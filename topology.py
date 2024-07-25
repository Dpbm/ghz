from qiskit.providers import Backend
from copy import deepcopy

class Node:
    def __init__(self, value:int, children:list):
        self.value = value
        self.children = children
    def __repr__(self):
        return (f"Node: {self.value}\nChildren: {[child.value for child in self.children]}")


class Path:
    def __init__(self, starting_node:Node):
        self.nodes = [starting_node]
        
    def add_node(self, node):
        self.nodes.append(node)

    @property
    def actual_node(self):
        return self.nodes[-1]

    @property
    def size(self):
        return len(self.nodes)

    @property
    def nodes_set(self):
        return {node.value for node in self.nodes}

    def __repr__(self):
        return ' '.join([str(node.value) for node in self.nodes])


class Topology:
    def __init__(self, backend:Backend, nodes: list[Node]):
        self.backend = backend
        self.nodes = nodes
        self.paths = []
    
    def map_nodes(self):
        edges = iter(self.backend.coupling_map.get_edges())
        for i,j in edges:
            self.nodes[i].children.append(self.nodes[j])

    def traverse(self):
        for node in self.nodes:
            backtrack = []
            path = Path(node)
            
            while True:
                children = path.actual_node.children
                total_children = len(children)

                if(total_children == 0):
                    if(len(backtrack) == 0):
                        self.paths.append(deepcopy(path))
                        break
                    else:
                        self.paths.append(deepcopy(path))
                        backtrack.pop()
                        if(len(backtrack) == 0):
                            break
                        else:
                            path = deepcopy(backtrack[-1])
                            backtrack.pop()
                    
                elif(total_children == 1):
                    actual_node = children[0]
                    path.add_node(actual_node)
                else:
                    for child in children:
                        new_path = deepcopy(path)
                        new_path.add_node(child)
                        backtrack.append(new_path)
                    path = deepcopy(backtrack[-1])
                    backtrack.pop()
                    
    def get_longest_path(self) -> Path:
        longest_path = self.paths[0]
        size = longest_path.size
        
        for path in self.paths:
            if(path.size > size):
                size = path.size
                longest_path = path
        return longest_path

    def get_desc_order_paths(self) -> list[Path]:
        return sorted(self.paths, key= lambda path: path.size, reverse=True)
                    
    def get_experiments_paths(self) -> list[Path]:
        paths = self.get_desc_order_paths()
        qubits = {i for i in range(self.backend.num_qubits)}
        selected_paths = []
        visited_paths = set()

        while len(qubits) > 0:
            biggest_change = 0
            path_i = 0
            best_path = paths[0]
            
            for i,path in enumerate(paths):
                if(i in visited_paths):
                    continue
                
                qubits_difference = len(qubits) - len(qubits - path.nodes_set) 
                if(qubits_difference > biggest_change):
                    biggest_change = qubits_difference
                    best_path = path
                    path_i = i

            visited_paths.add(path_i)
            selected_paths.append(best_path)
            qubits -= best_path.nodes_set

        return selected_paths