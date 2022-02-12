import numpy as np
from qiskit import *


def myh(qc, n):
    """
    Define H gate as a convenient tool to improve readability.
    """
    qc.rx(np.pi, n)
    qc.ry(-np.pi / 2, n)
    return qc


def myt(qc, n):
    """
    Define T gate as a convenient tool to improve readability.
    """
    qc.rx(-np.pi / 2, n)
    qc.ry(np.pi / 4, n)
    qc.rx(+np.pi / 2, n)
    return qc


def mytdg(qc, n):
    """
    Define Tdgr gate as a convenient tool to improve readability.
    """
    qc.rx(-np.pi / 2, n)
    qc.ry(-np.pi / 4, n)
    qc.rx(+np.pi / 2, n)
    return qc


def exercise3():
    q = QuantumRegister(3)
    qc = QuantumCircuit(q)

    # Implement tofolli gate using the decomposition provided in the
    # qiskit textbook.
    myh(qc, 2)

    qc.cx(1, 2)

    mytdg(qc, 2)
    qc.cx(0, 2)

    myt(qc, 2)
    qc.cx(1, 2)

    mytdg(qc, 2)
    qc.cx(0, 2)

    myt(qc, 1)
    myt(qc, 2)
    myh(qc, 2)
    qc.cx(0, 1)

    myt(qc, 0)
    mytdg(qc, 1)
    qc.cx(0, 1)
    return qc
