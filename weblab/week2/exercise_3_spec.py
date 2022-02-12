import unittest
from qiskit.quantum_info import Statevector
from qiskit import *
import solution
import numpy as np

EPSILON = 0.01
import weblabTestRunner

validGates = (qiskit.circuit.library.U1Gate, qiskit.circuit.library.U2Gate, qiskit.circuit.library.U3Gate)


class TestSolution(unittest.TestCase):
	# def setUp(self):
	#    print(1)

	# Place all the tests between the START comment and the END comment.
	# Do not remove the TESTS comments

	# TESTS START HERE

	# Any future programmers: Don't do this. Workaround to allow weblab to give a nice distribution of grades.
	def test_correctness_0(self):
		p0target = 0
		qc = solution.exercise3(p0target)

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates), g[0])

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)
		vector = job.result().get_statevector(qc, decimals=8)

		p0 = np.abs(np.inner(vector, [1., 1.]) / np.sqrt(2)) ** 2
		p1 = np.abs(np.inner(vector, [1., -1.]) / np.sqrt(2)) ** 2

		variationalDistance = np.abs(p0 - p0target) + np.abs(p1 - (1 - p0target))

		self.assertTrue(variationalDistance < EPSILON, p0target)

	def test_correctness_1(self):
		p0target = 1
		qc = solution.exercise3(p0target)

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates), g[0])

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)
		vector = job.result().get_statevector(qc, decimals=8)

		p0 = np.abs(np.inner(vector, [1., 1.]) / np.sqrt(2)) ** 2
		p1 = np.abs(np.inner(vector, [1., -1.]) / np.sqrt(2)) ** 2

		variationalDistance = np.abs(p0 - p0target) + np.abs(p1 - (1 - p0target))

		self.assertTrue(variationalDistance < EPSILON, p0target)

	def test_correctness_2(self):
		p0target = 0.1
		qc = solution.exercise3(p0target)

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates), g[0])

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)
		vector = job.result().get_statevector(qc, decimals=8)

		p0 = np.abs(np.inner(vector, [1., 1.]) / np.sqrt(2)) ** 2
		p1 = np.abs(np.inner(vector, [1., -1.]) / np.sqrt(2)) ** 2

		variationalDistance = np.abs(p0 - p0target) + np.abs(p1 - (1 - p0target))

		self.assertTrue(variationalDistance < EPSILON, p0target)

	def test_correctness_3(self):
		p0target = 0.2
		qc = solution.exercise3(p0target)

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates), g[0])

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)
		vector = job.result().get_statevector(qc, decimals=8)

		p0 = np.abs(np.inner(vector, [1., 1.]) / np.sqrt(2)) ** 2
		p1 = np.abs(np.inner(vector, [1., -1.]) / np.sqrt(2)) ** 2

		variationalDistance = np.abs(p0 - p0target) + np.abs(p1 - (1 - p0target))

		self.assertTrue(variationalDistance < EPSILON, p0target)

	def test_correctness_4(self):
		p0target = 0.3
		qc = solution.exercise3(p0target)

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates), g[0])

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)
		vector = job.result().get_statevector(qc, decimals=8)

		p0 = np.abs(np.inner(vector, [1., 1.]) / np.sqrt(2)) ** 2
		p1 = np.abs(np.inner(vector, [1., -1.]) / np.sqrt(2)) ** 2

		variationalDistance = np.abs(p0 - p0target) + np.abs(p1 - (1 - p0target))

		self.assertTrue(variationalDistance < EPSILON, p0target)

	def test_correctness_5(self):
		p0target = 0.4
		qc = solution.exercise3(p0target)

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates), g[0])

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)
		vector = job.result().get_statevector(qc, decimals=8)

		p0 = np.abs(np.inner(vector, [1., 1.]) / np.sqrt(2)) ** 2
		p1 = np.abs(np.inner(vector, [1., -1.]) / np.sqrt(2)) ** 2

		variationalDistance = np.abs(p0 - p0target) + np.abs(p1 - (1 - p0target))

		self.assertTrue(variationalDistance < EPSILON, p0target)

	def test_correctness_6(self):
		p0target = 0.5
		qc = solution.exercise3(p0target)

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates), g[0])

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)
		vector = job.result().get_statevector(qc, decimals=8)

		p0 = np.abs(np.inner(vector, [1., 1.]) / np.sqrt(2)) ** 2
		p1 = np.abs(np.inner(vector, [1., -1.]) / np.sqrt(2)) ** 2

		variationalDistance = np.abs(p0 - p0target) + np.abs(p1 - (1 - p0target))

		self.assertTrue(variationalDistance < EPSILON, p0target)

	def test_correctness_7(self):
		p0target = 0.6
		qc = solution.exercise3(p0target)

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates), g[0])

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)
		vector = job.result().get_statevector(qc, decimals=8)

		p0 = np.abs(np.inner(vector, [1., 1.]) / np.sqrt(2)) ** 2
		p1 = np.abs(np.inner(vector, [1., -1.]) / np.sqrt(2)) ** 2

		variationalDistance = np.abs(p0 - p0target) + np.abs(p1 - (1 - p0target))

		self.assertTrue(variationalDistance < EPSILON, p0target)

	def test_correctness_8(self):
		p0target = 0.7
		qc = solution.exercise3(p0target)

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates), g[0])

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)
		vector = job.result().get_statevector(qc, decimals=8)

		p0 = np.abs(np.inner(vector, [1., 1.]) / np.sqrt(2)) ** 2
		p1 = np.abs(np.inner(vector, [1., -1.]) / np.sqrt(2)) ** 2

		variationalDistance = np.abs(p0 - p0target) + np.abs(p1 - (1 - p0target))

		self.assertTrue(variationalDistance < EPSILON, p0target)

	def test_number_of_gates(self):
		# Check number of gates used
		for i in range(11):
			p0target = i * 0.1
			qc = solution.exercise3(p0target)
			self.assertTrue(len(qc.data) < 2)

		p0target = 0.6
		qc = solution.exercise3(p0target)

		for g in qc.data:
			self.assertTrue(isinstance(g[0], validGates), g[0])

		backend = Aer.get_backend('statevector_simulator')
		job = execute(qc, backend)
		vector = job.result().get_statevector(qc, decimals=8)

		p0 = np.abs(np.inner(vector, [1., 1.]) / np.sqrt(2)) ** 2
		p1 = np.abs(np.inner(vector, [1., -1.]) / np.sqrt(2)) ** 2

		variationalDistance = np.abs(p0 - p0target) + np.abs(p1 - (1 - p0target))

		self.assertTrue(variationalDistance < EPSILON, p0target)


# TESTS END HERE


if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.TestRunner)