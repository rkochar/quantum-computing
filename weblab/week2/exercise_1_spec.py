import unittest
from qiskit.quantum_info import Statevector
from qiskit import *
import solution
import numpy as np

EPSILON = 0.01
import weblabTestRunner


class TestSolution(unittest.TestCase):
	# def setUp(self):
	#    print(1)

	# Place all the tests between the START comment and the END comment.
	# Do not remove the TESTS comments

	# TESTS START HERE
	def test_correct_unitary(self):
		studentQC = solution.exercise1()

		q = QuantumRegister(1)
		qc = QuantumCircuit(q)  # create circuit
		qc.h(q[0])  # add Hadamard gate

		backend = Aer.get_backend('unitary_simulator')
		job = execute(qc, backend)
		studentJob = execute(studentQC, backend)

		unitary = job.result().get_unitary(qc, decimals=3)
		studentUnitary = studentJob.result().get_unitary(studentQC, decimals=3)

		idtarget = np.matmul(unitary, studentUnitary.conjugate().transpose())
		input_dim = 2
		processFidelity = np.abs(np.trace(idtarget) / input_dim) ** 2

		self.assertTrue(processFidelity > 1 - EPSILON)

	def test_hadamard_self_inverse(self):
		studentQC = solution.exercise1()
		studentQC.h(0)

		backend = Aer.get_backend('unitary_simulator')
		job = execute(studentQC, backend)
		studentJob = execute(studentQC, backend)

		studentUnitary = studentJob.result().get_unitary(studentQC, decimals=3)

		input_dim = 2
		processFidelity = np.abs(np.trace(studentUnitary) / input_dim) ** 2

		assert processFidelity > 1 - EPSILON


# TESTS END HERE


if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.TestRunner)