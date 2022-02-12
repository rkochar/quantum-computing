import numpy as np
from qiskit import *


def exercise3():
    q = QuantumRegister(3)
    qc = QuantumCircuit(q)
    ## BEGIN SOLUTION
    qc.ccx(0, 1, 2)
    qc.cx(0, 1)
    ## END SOLUTION
    return qc