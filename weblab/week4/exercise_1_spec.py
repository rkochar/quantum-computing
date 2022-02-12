import unittest
from qiskit.quantum_info import Statevector
from qiskit import *
from qiskit.circuit.library import CXGate, SGate, RXGate
import solution
import numpy as np
from decorators import required_spectest, spectest
import weblabTestRunner

backend = Aer.get_backend('unitary_simulator')
validGates = (CXGate, RXGate, SGate)
EPSILON = 1e-6


class TestSolution(unittest.TestCase):

	# Place all the tests between the START comment and the END comment.
	# Do not remove the TESTS comments

	# TESTS START HERE

	@spectest(20)
	@required_spectest(100)
	def test_correct_implementation(self) -> None:
		"""
		Spectest is set to required, as only good implementations are eligible for more points.
		Student tests don't have this requirement to let students fiddle around in their implementation.
		"""
		qc = solution.exercise1()
		self.assertGreater(len(qc.data), 0)
		qc.ccx(*range(3))
		qc.x(2)
		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)
		processFidelity = np.abs(np.trace(unitary) / 8) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)

	@spectest(5)
	def test_valid_gates(self) -> None:
		"""
		Succeeding this spec test results in an additional 5 points, as described in the assignment. Indicative
		that the student implemented the qNAND gate with the prescribed gate set.
		"""
		qc = solution.exercise1()
		filtered_gates = [g for g in qc.data if not isinstance(g[0], validGates)]
		self.assertEqual(len(filtered_gates), 0)

	@spectest(10)
	def test_minimum_number_gates_total(self) -> None:
		"""
		Succeeding this spectest means that the student succesfully completed the exercise, with valid gates and
		at most the minimum number of gates used for their implementation.
		"""
		self.test_valid_gates()
		qc = solution.exercise1()
		# Assert at most 50 gates are used in the implementation
		self.assertLess(len(qc.data), 51)

		# Assert at most 7 CX gates are used (provably optimal Toffoli)
		cx_count = len(list(filter(lambda x: isinstance(x[0], CXGate), qc.data)))
		self.assertEqual(cx_count, 6)


# TESTS END HERE

if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)


