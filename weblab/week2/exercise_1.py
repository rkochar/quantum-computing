from qiskit.quantum_info import Statevector
import numpy as np
from qiskit import *

def exercise1(): # Create QC
    q = QuantumRegister(1)
    qc = QuantumCircuit(q) # create circuit
    qc.h(q)
    return qc
