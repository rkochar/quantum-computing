from qiskit.quantum_info import Statevector
import numpy as np
from qiskit import *


def h_gate():
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)
    # Multiply Rx and Ry and solve for Theta and Phi
    qc.ry(np.pi/2, 0)
    qc.rx(np.pi, 0)
    return qc

def s_gate():
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)
    # S gate is Rz(pi/2)
    # Rx = H Rz H
    # Rz = H Rx H
    # H from above.
    qc.ry(np.pi/2, 0)
    qc.rx(np.pi, 0) # H
    qc.rx(np.pi/2, 0) # Rotate half pi
    qc.ry(np.pi/2, 0) # H
    qc.rx(np.pi, 0)
    return qc

def t_gate():
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)
    # Same as above, except the angle is pi / 4
    qc.ry(np.pi/2, 0)
    qc.rx(np.pi, 0) # H
    qc.rx(np.pi/4, 0) # Rotate pi/4
    qc.ry(np.pi/2, 0) # H
    qc.rx(np.pi, 0)
    return qc