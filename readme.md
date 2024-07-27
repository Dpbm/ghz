# GHZ

This repo contains some tests on creating `GHZ` states using [Qiskit](https://www.ibm.com/quantum/qiskit).

For this project, the idea was to explore some different techniques to create big `GHZ states`.

The techniques I used were:

- circuit knitting
- topology mapping
- circuit transpilation (using Qiskit `PassManager` and `Sampler`)

In total, 4 circuits were built mixing some of these techniques.

## Circuits

### 5 qubits GHZ - [notebook](./circuit-cutting-test.ipynb)

![GHZ 5 qubits circuit](./5-qubits-GHZ-circuit.png)

This one was the first test done with circuit knitting, using the `cutqc` module from `circuit knitting toolbox` package.

Here the circuit was cut in 2 separated parts, measured and them joined together.

![GHZ 5 qubits dists](./5-qubits-GHZ-circuit-cutting-test.png)

| cuts                                          |  exported data                                                        |
|-----------------------------------------------|-----------------------------------------------------------------------|
|[subcircuit 0](./5-qubits-GHZ-subcircuit-0.qpy)|[cuts](./5-qubits-GHZ-cuts.json)                                       |
|[subcircuit 1](./5-qubits-GHZ-subcircuit-1.qpy)|[probabilities](./5-qubits-GHZ-probs.json)                             |
|                                               |[reconstructed probabilities](./5-qubits-GHZ-reconstructed-probs.json) |


### 16 qubits GHZ - [notebook](./16-qubits-ghz-circuit-knitting.ipynb)

![GHZ 16 qubits circuit](./16-qubits-GHZ-circuit.png)

The second is a 16 qubits circuit, following the topology of IBM's Guadalupe backend. After mapping each qubit connection, the resulting distribution after simulating was:

![GHZ 16 qubits IBM Guadalupe simulation](./16-qubits-GHZ-counts.png)

This one, was also cut using `cutqc` giving the following results:

![GHZ 16 qubits cut result](./16-qubits-GHZ-circuit-cutting.png)

| cuts                                           |  exported data                                                        |
|------------------------------------------------|-----------------------------------------------------------------------|
|[subcircuit 0](./16-qubits-GHZ-subcircuit-0.qpy)|[cuts](./16-qubits-GHZ-cuts.json)                                      |
|[subcircuit 1](./16-qubits-GHZ-subcircuit-1.qpy)|[probabilities](./16-qubits-GHZ-probs.json)                            |
|[subcircuit 2](./16-qubits-GHZ-subcircuit-2.qpy)|[reconstructed probabilities](./16-qubits-GHZ-reconstructed-probs.json)|

## 28 qubits GHZ - [notebook](./28-qubits-ghz-circuit-knitting.ipynb)

![GHZ 28 qubits circuit](./28-qubits-GHZ-circuit.png)

The 28 qubits version was based on IBM's Cambridge backend, however this one wasn't executed due to hardware issues.
Nevertheless, some cuts were done.

| cuts                                           |  exported data                                                        |
|------------------------------------------------|-----------------------------------------------------------------------|
|[subcircuit 0](./28-qubits-GHZ-subcircuit-0.qpy)|[cuts](./28-qubits-GHZ-cuts.json)                                      |
|[subcircuit 1](./28-qubits-GHZ-subcircuit-1.qpy)|[probabilities](./28-qubits-GHZ-probs.json)                            |
|[subcircuit 2](./28-qubits-GHZ-subcircuit-2.qpy)|                                                                       |
|[subcircuit 3](./28-qubits-GHZ-subcircuit-3.qpy)|                                                                       |

## 127 qubits GHZ - [notebook](./ghz-127-qubits.ipynb)

![GHZ 127 qubits circuit](./127-qubits-GHZ-circuit.png)

The biggest one, is based on IBM's Osaka backend. This one, was transpiled and executed on real hardware, the outcomes were the following:

![osaka results](./127-qubits-GHZ-counts.png)

These results seem really wrong, once the expected was nearly 50% of probability for $|00000...0\rangle$ and 50% for $|11111...1\rangle$. However, due the amount of errors for `cx` gates, it's probably the accurate result for a real device.

This effect can be seem in a local test executed with 20 qubits.

![osaka 20 qubits](./test-osaka-ghz-state-20-qubit.png)

![osaka 20 qubits counts](./20-qubits-ghz-counts-local-job.png)

Even that the extreme states are with high probability, it tends to deviate at each qubit addition.