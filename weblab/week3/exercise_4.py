from qiskit.quantum_info import Statevector
import numpy as np
from qiskit import *

def exercise4():
    q = QuantumRegister(2)
    qc = QuantumCircuit(q)
    ### BEGIN SOLUTION
    qc.cx(1, 0)
    qc.rz(-np.pi / 8, 0)
    qc.cx(1, 0)
    qc.rz(np.pi / 8, 0)
    # qc.cu1(np.pi/4,1,0)
    ### END SOLUTION
    return qc
