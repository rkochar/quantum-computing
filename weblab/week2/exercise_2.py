from qiskit.quantum_info import Statevector
import numpy as np
from qiskit import *

def exercise2(): # Apply T's and H's until you get |0> + e^-ipi/4
    q = QuantumRegister(1)
    qc = QuantumCircuit(q) # create circuit
    qc.h(q) # |+> = (|0> + |1>)/sqrt(2)
    qc.t(q) # (|0> + e^ipi/4|1>)/sqrt(2)
    qc.t(q) # (|0> + e^2ipi/4|1>)/sqrt(2)
    qc.t(q) # (|0> + e^3ipi/4|1>)/sqrt(2) etc.
    qc.t(q)
    qc.t(q)
    qc.t(q)
    qc.t(q)
    # Also possible to implement this with H and Tdg
    return qc