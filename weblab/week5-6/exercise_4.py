import numpy as np
from qiskit import QuantumCircuit, QuantumRegister


def transformation(n):
    qc = QuantumCircuit(n)

    # BEGIN SOLUTION
    qc.h(range(n))
    return qc
