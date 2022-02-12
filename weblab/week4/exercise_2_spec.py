import unittest
from qiskit import *
import solution
from library import *
import numpy as np
import weblabTestRunner
from decorators import spectest

backend = Aer.get_backend('unitary_simulator')
EPSILON = 1e-6


class TestSolution(unittest.TestCase):
	# Place all the tests between the START comment and the END comment.
	# Do not remove the TESTS comments

	# TESTS START HERE

	@spectest(1)
	def test_nand_gate(self):
		def nand(binList):
			a = binList[0]
			b = binList[1]
			return [(a & b) ^ 1]

		qc = solution.exercise2(nand, 2, 1)

		# Reverse action and check for identity
		qc.ccx(0, 1, 2)
		qc.x(2)

		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)

		processFidelity = np.abs(np.trace(unitary) / 8) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)

	# @spectest(1)
	# def test_sum_2_bits(self):
	#     def sum2bits(binList):
	#         a = binList[0]
	#         b = binList[1]
	#         return [(a & b), a ^ b]
	#         #return [(a ^ b), a & b]

	#     qc = solution.exercise2(sum2bits, 2, 2)

	#     # Reverse action and check for identity
	#     qc.ccx(0, 1, 3)
	#     qc.cx(0, 2)
	#     qc.cx(1, 2)

	#     job = execute(qc, backend)
	#     unitary = job.result().get_unitary(qc, decimals=8)

	#     processFidelity = np.abs(np.trace(unitary) / 16) ** 2
	#     self.assertGreater(processFidelity, 1 - EPSILON)

	@spectest(1)
	def test_input_length(self):
		def f(binList):
			return [0] * len(binList)

		qc = solution.exercise2(f, 5, 5)

		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)

		processFidelity = np.abs(np.trace(unitary) / 4 ** (5)) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)

	@spectest(5)
	def test_identity(self):
		def f(x):
			return x

		qc = solution.exercise2(f, 1, 1)
		qc.cx(0, 1)

		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)

		processFidelity = np.abs(np.trace(unitary) / 4) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)

	@spectest(5)
	def test_not_gate(self):
		def f(binList):
			return [e ^ 1 for e in binList]

		qc = solution.exercise2(f, 1, 1)
		qc.x(0)
		qc.cx(0, 1)
		qc.x(0)

		job = execute(qc, backend)
		unitary = job.result().get_unitary(qc, decimals=8)

		processFidelity = np.abs(np.trace(unitary) / 4) ** 2
		self.assertGreater(processFidelity, 1 - EPSILON)

# @spectest(5)
# def test_hamming_weight(self):
#     np.set_printoptions(threshold=sys.maxsize)
#     def f(binList):
#         return int2bin(sum(binList), 2)

#     # Mjam, partially apply the function.
#     qc = solution.exercise2(f, 2, 3)

#     # qc.cx(0, 4)
#     # qc.cx(1, 4)
#     # qc.cx(2, 4)

#     # qc.ccx(0, 1, 3)
#     # qc.ccx(0, 2, 3)
#     # qc.ccx(1, 2, 3)

#     qc.cx(2, 0)
#     qc.cx(3, 0)
#     qc.cx(4, 0)

#     qc.ccx(2, 3, 1)
#     qc.ccx(3, 4, 1)
#     qc.ccx(2, 4, 1)
#     print(qc.draw())
#     job = execute(qc, backend)
#     unitary = job.result().get_unitary(qc, decimals=8)
#     print(unitary)

#     processFidelity = np.abs(np.trace(unitary) / (2 ** 5))**2
#     self.assertGreater(processFidelity, 1 - EPSILON)


# TESTS END HERE


if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
