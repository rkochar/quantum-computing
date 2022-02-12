import unittest
from qiskit import *
from qiskit.circuit.library import CXGate, RXGate, RYGate
import solution
import numpy as np
import weblabTestRunner
from decorators import *

backend = Aer.get_backend('unitary_simulator')
validGates = (CXGate, RXGate, RYGate)
EPSILON = 1e-6


class TestSolution(unittest.TestCase):
	# def setUp(self):
	#    print(1)

	# Place all the tests between the START comment and the END comment.
	# Do not remove the TESTS comments

	# TESTS START HERE
	@spectest(30)
	@required_spectest(100)
	def test_correct_gate_set(self):
		qc = solution.exercise3()

		for g in qc.data:  # Check type of gates used
			self.assertTrue(isinstance(g[0], validGates), g[0])

	@spectest(50)
	def test_validate_circuit(self):
		qc = solution.exercise3()
		qc.ccx(0, 1, 2)
		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)
		processFidelity = np.abs(np.trace(unitary) / 8) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)

	@spectest(10)
	def test_gate_count(self):
		qc = solution.exercise3()

		for g in qc.data:  # Check type of gates used
			self.assertTrue(isinstance(g[0], validGates), g[0])
		self.assertLess(len(qc.data), 32)

	@spectest(10)
	def test_cnot_count(self):
		qc = solution.exercise3()
		cx_count = len(list(filter(lambda x: isinstance(x[0], CXGate), qc.data)))
		self.assertEqual(cx_count, 6)


# TESTS END HERE
if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
