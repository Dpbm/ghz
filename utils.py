from qiskit.circuit import Qubit
import numpy as np

def qubit_to_dict(qubit:Qubit) -> dict:
    reg = qubit._register
    return {
        "index":qubit._index, 
        'register': {
            'name': reg.name,
            'size': reg.size
        }
    }

def qubit_to_str(qubit:Qubit) -> str:
    reg = qubit._register
    return f'{reg.name}{reg.size}-i{qubit._index}'


def save_cuts(cuts:dict, prefix:str):
    import json
    from copy import deepcopy
    from qiskit import qpy
    
    cuts_to_save = deepcopy(cuts)
    subcircuits_overwrite = []
    
    for i,subcircuit in enumerate(cuts_to_save['subcircuits']):
        subcircuit_filename = f'{prefix}-subcircuit-{i}.qpy'
        with open(subcircuit_filename, 'wb') as file:
            qpy.dump(subcircuit, file)
            
        subcircuits_overwrite.append(subcircuit_filename)
        
    cuts_to_save['subcircuits'] = subcircuits_overwrite

    path_map_overwrite = {}
    path_map = cuts_to_save['complete_path_map']
    
    for qubit,data in path_map.items():
        qubit_name = qubit_to_str(qubit)
        
                
        path_map_overwrite[qubit_name] = {
            'qubit_data': qubit_to_dict(qubit),
            qubit_name: [],
        }

        for subcircuits_data in data:
            qubit_subcircuit_data = {}
            for key,val in subcircuits_data.items():
                if(key == 'subcircuit_qubit'):
                    qubit_subcircuit_data[key] = qubit_to_dict(val)
                else:
                    qubit_subcircuit_data[key] = val
            path_map_overwrite[qubit_name][qubit_name].append(qubit_subcircuit_data)
            
    cuts_to_save['complete_path_map'] = path_map_overwrite


    print("Saving cuts as JSON...")
    with open(f"{prefix}-cuts.json", "w") as file:
        json.dump(cuts_to_save,file)

def save_probs(probs:dict, prefix:str):
    import json

    data = {}
    for key, prob_values in probs.items():
        data[key] = {}
        for prob_index, prob_array in prob_values.items():
            data[key][prob_index] = prob_array.tolist()
    
    print("Saving probabilities as JSON...")
    with open(f"{prefix}-probs.json", "w") as file:
        json.dump(data,file)

def save_reconstructed_probs(probs:np.ndarray, prefix:str):
    import json

    data = {
        "dist": probs.tolist()
    }
    
    print("Saving reconstructed probabilities as JSON...")
    with open(f"{prefix}-reconstructed-probs.json", "w") as file:
        json.dump(data,file)

def save_obj(obj:dict, filename:str):
    import json
    print("Saving object as JSON...")
    with open(filename, "w") as file:
        json.dump(obj,file)