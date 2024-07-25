from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime.fake_provider import FakeCambridgeV2, FakeGuadalupeV2
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from dotenv import load_dotenv
import os

load_dotenv()
QiskitRuntimeService.save_account(channel="ibm_quantum", token=os.getenv("IBM_TOKEN"), overwrite=True)

service = QiskitRuntimeService()

osaka_backend = service.backend("ibm_osaka")
fake_backend_cambridge = FakeCambridgeV2()
fake_backend_guadalupe = FakeGuadalupeV2()

transpiler_real_backend = generate_preset_pass_manager(optimization_level=3, backend=osaka_backend)
sampler_real_backend = SamplerV2(osaka_backend)

transpiler_fake_backend_cambridge = generate_preset_pass_manager(optimization_level=3, backend=fake_backend_cambridge)
sampler_fake_backend_cambridge = SamplerV2(fake_backend_cambridge)

transpiler_fake_backend_guadalupe = generate_preset_pass_manager(optimization_level=3, backend=fake_backend_guadalupe)
sampler_fake_backend_guadalupe = SamplerV2(fake_backend_guadalupe)