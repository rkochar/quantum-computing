from qiskit.quantum_info import Statevector
import numpy as np
from qiskit import *

def exercise3(x): # RNG Transform
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)
    qc.u3(np.pi/2, 2 * np.arccos(np.sqrt(x)), 0, 0)
    return qc
