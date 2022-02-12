import numpy as np
from qiskit import *


def exercise2(perm):
    q = QuantumRegister(len(perm))
    qc = QuantumCircuit(q)
    n = len(perm)
    for idx in range(n):
        nxt = idx
        while perm[nxt] >= 0:
            if idx != perm[nxt]:
                qc.cx(idx, perm[nxt])
                qc.cx(perm[nxt], idx)
                qc.cx(idx, perm[nxt])
            temp = perm[nxt]
            perm[nxt] -= n
            nxt = temp
    return qc
