import numpy as np
from qiskit import *


def qft(n):
    qc = QuantumCircuit(n)
    # BEGIN SOLUTION
    # construct the answer
    omega = np.exp(complex(0.0, 2.0 * np.pi / (2 ** n)))
    ans = np.zeros((2 ** n, 2 ** n), dtype=complex)
    norm = np.sqrt(2 ** n)
    for i in range(2 ** n):
        for j in range(2 ** n):
            ans[i][j] = pow(omega, i * j) / norm
    qc.unitary(ans, range(n))
    # print(ans)
    # END SOLUTION
    return qc
