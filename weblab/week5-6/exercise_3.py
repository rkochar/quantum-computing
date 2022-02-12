from qiskit import QuantumCircuit
import numpy as np


def phase_oracle(uf, n, phi):
    qc = QuantumCircuit(n + 1)

    # BEGIN SOLUTION
    if phi == np.pi:
        qc.x(n)
        qc.h(n)
        qc = qc + uf
        qc.h(n)
        qc.x(n)
    else:
        qc = qc + uf
        qc.u1(phi, n)
        qc = qc + uf
    return qc
