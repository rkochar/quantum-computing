import unittest
from qiskit.quantum_info import Statevector
from qiskit import *
import solution
import numpy as np

EPSILON = 0.01
import weblabTestRunner

validGates = (qiskit.circuit.library.HGate, qiskit.circuit.library.TGate)


class TestSolution(unittest.TestCase):
	# def setUp(self):
	#    print(1)

	# Place all the tests between the START comment and the END comment.
	# Do not remove the TESTS comments

	# TESTS START HERE

	def test_correctness(self):
		qc = solution.exercise2()

		qc.t(0)
		qc.h(0)

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)

		vector = job.result().get_statevector(qc, decimals=3)
		fidelity = np.abs(np.inner(vector, [1., 0.])) ** 2

		self.assertTrue(fidelity > 1 - EPSILON)

	def test_complete_correctness(self):
		qc = solution.exercise2()

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates))

		qc.t(0)
		qc.h(0)

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)

		vector = job.result().get_statevector(qc, decimals=3)
		fidelity = np.abs(np.inner(vector, [1., 0.])) ** 2

		self.assertTrue(fidelity > 1 - EPSILON)

	def test_gates_used(self):
		qc = solution.exercise2()

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates))

	def test_number_of_gates(self):
		# Check number of gates used
		qc = solution.exercise2()
		self.assertTrue(len(qc.data) < 11)


# TESTS END HERE


if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.TestRunner)