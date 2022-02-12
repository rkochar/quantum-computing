import numpy as np
from qiskit import *


def myh(qc, n):
    qc.s(n)
    qc.rx(np.pi / 2, n)
    qc.s(n)
    return qc


def myt(qc, n):
    qc.rx(np.pi / 2, n)
    qc.s(n)
    qc.rx(np.pi + np.pi / 4, n)
    qc.s(n)
    qc.rx(np.pi / 2, n)
    return qc


def mytdg(qc, n):
    qc.rx(np.pi / 2, n)
    qc.s(n)
    qc.rx(np.pi - np.pi / 4, n)
    qc.s(n)
    qc.rx(np.pi / 2, n)
    return qc


def mytoffoli(qc):
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


def exercise1():
    q = QuantumRegister(3)
    qc = QuantumCircuit(q)
    ### BEGIN SOLUTION
    qc = mytoffoli(qc)
    qc.rx(np.pi, 2)
    ### END SOLUTION
    return qc
