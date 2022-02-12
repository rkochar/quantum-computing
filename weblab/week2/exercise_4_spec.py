import unittest
from qiskit.quantum_info import Statevector
from qiskit import *
from solution import h_gate, t_gate, s_gate
import numpy as np

EPSILON = 0.01
input_dim = 2
backend = backend = Aer.get_backend('unitary_simulator')
validGates = (qiskit.circuit.library.RXGate, qiskit.circuit.library.RYGate, qiskit.circuit.library.RZGate)
minimumGates = (qiskit.circuit.library.RXGate, qiskit.circuit.library.RYGate)
import weblabTestRunner


class TestSolution(unittest.TestCase):

	# Place all the tests between the START comment and the END comment.
	# Do not remove the TESTS comments

	# TESTS START HERE

	def test_h_correct(self):
		qc = h_gate()
		for g in qc.data:  # Check type of gates used
			self.assertTrue(isinstance(g[0], validGates), g[0])
		qc.h(0)
		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)

		processFidelity = np.abs(np.trace(unitary) / input_dim) ** 2
		self.assertTrue(processFidelity > 1 - EPSILON)

	def test_s_correct(self):
		qc = s_gate()
		for g in qc.data:  # Check type of gates used
			self.assertTrue(isinstance(g[0], validGates), g[0])
		qc.sdg(0)
		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)

		processFidelity = np.abs(np.trace(unitary) / input_dim) ** 2
		self.assertTrue(processFidelity > 1 - EPSILON)

	def test_t_correct(self):
		qc = t_gate()
		for g in qc.data:  # Check type of gates used
			self.assertTrue(isinstance(g[0], validGates), g[0])
		qc.tdg(0)
		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)

		processFidelity = np.abs(np.trace(unitary) / input_dim) ** 2
		self.assertTrue(processFidelity > 1 - EPSILON)

	def test_h_correct_minimal(self):
		qc = h_gate()
		for g in qc.data:  # Check type of gates used
			self.assertTrue(isinstance(g[0], minimumGates), g[0])
		qc.h(0)
		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)

		processFidelity = np.abs(np.trace(unitary) / input_dim) ** 2
		self.assertTrue(processFidelity > 1 - EPSILON)

	def test_s_correct_minimal(self):
		qc = s_gate()
		for g in qc.data:  # Check type of gates used
			self.assertTrue(isinstance(g[0], minimumGates), g[0])
		qc.sdg(0)
		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)

		processFidelity = np.abs(np.trace(unitary) / input_dim) ** 2
		self.assertTrue(processFidelity > 1 - EPSILON)

	def test_t_correct_minimal(self):
		qc = t_gate()
		for g in qc.data:  # Check type of gates used
			self.assertTrue(isinstance(g[0], minimumGates), g[0])
		qc.tdg(0)
		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)

		processFidelity = np.abs(np.trace(unitary) / input_dim) ** 2
		self.assertTrue(processFidelity > 1 - EPSILON)


# TESTS END HERE


if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.TestRunner)