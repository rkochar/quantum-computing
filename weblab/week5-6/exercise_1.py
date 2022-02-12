from qiskit import QuantumCircuit, QuantumRegister
import numpy as np


def rotate(n):
	q = QuantumRegister(n + 1)
	qc = QuantumCircuit(q)

	# BEGIN SOLUTION
	for x in range(n):
		qc.cp(np.pi * 2 ** (x - n + 1), x, n)

	return qc
