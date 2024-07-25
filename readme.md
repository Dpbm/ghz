# GHZ

This repo contains some tests on creating GHZ states using Qiskit.

In this project, I'm using some different techniques, like circuit knitting and topology mapping.

## 5 qubits GHZ

![GHZ 5 qubits circuit](./5-qubits-GHZ-circuit.png)

This one was the first test using circuit knitting, using the `cutqc` module from `circuit knitting toolbox` package.

In this one, the circuit was cut in 2 separated parts, measured and them joined together.

![GHZ 5 qubits dists](./5-qubits-GHZ-circuit-cutting-test.png)

## 28 qubits GHZ

![GHZ 28 qubits circuit](./28-qubits-GHZ-circuit.png)

## 127 qubits GHZ

![GHZ 127 qubits circuit](./127-qubits-GHZ-circuit.png)
