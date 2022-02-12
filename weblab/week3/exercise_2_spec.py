import unittest
from qiskit import *
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import CXGate
import solution
import numpy as np
import weblabTestRunner
from decorators import spectest, required_spectest

backend = Aer.get_backend('unitary_simulator')
validGates = (CXGate)
EPSILON = 1e-6


class TestSolution(unittest.TestCase):
	# def setUp(self):
	#    print(1)

	# Place all the tests between the START comment and the END comment.
	# Do not remove the TESTS comments

	# TESTS START HERE
	@spectest(5)
	@required_spectest(100)
	def test_correct_gate_set(self):
		perm = [0, 3, 5, 4, 2, 1]
		qc = solution.exercise2(perm)

		for g in qc.data:  # Check type of gates used
			self.assertTrue(isinstance(g[0], validGates), g[0])

	@spectest(5)
	def test_normal_order(self):
		perm = [0, 1]
		dim = 2 ** len(perm)
		qc = solution.exercise2(perm)

		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)
		processFidelity = np.abs(np.trace(unitary) / dim) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)

	@spectest(5)
	def test_reverse_order(self):
		perm = [1, 0]
		dim = 2 ** len(perm)
		qc = solution.exercise2(perm)

		qc.swap(0, 1)

		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)
		processFidelity = np.abs(np.trace(unitary) / dim) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)

	@spectest(5)
	def test_three_normal(self):
		perm = [0, 1, 2]
		dim = 2 ** len(perm)
		qc = solution.exercise2(perm)

		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)
		processFidelity = np.abs(np.trace(unitary) / dim) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)

	@spectest(5)
	def test_three_swapped(self):
		perm = [1, 2, 0]
		dim = 2 ** len(perm)
		qc = solution.exercise2(perm)

		# Fix the permutation
		qc.swap(0, 2)
		qc.swap(0, 1)

		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)
		processFidelity = np.abs(np.trace(unitary) / dim) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)

	@spectest(5)
	def test_ten_swapped(self):
		perm = [0, 1, 2, 3, 4, 5, 8, 6, 7, 9, 10]
		dim = 2 ** len(perm)
		qc = solution.exercise2(perm)

		# Fix the permutation
		qc.swap(6, 7)
		qc.swap(6, 8)

		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)
		processFidelity = np.abs(np.trace(unitary) / dim) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)


# TESTS END HERE


if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
