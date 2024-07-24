from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService

_service = QiskitRuntimeService()
osaka_backend = _service.backend("ibm_osaka")
fake_osaka_backend = AerSimulator.from_backend(osaka_backend)
transpiler = generate_preset_pass_manager(optimization_level=3, backend=fake_osaka_backend)