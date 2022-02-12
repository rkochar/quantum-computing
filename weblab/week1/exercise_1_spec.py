import unittest
from qiskit.quantum_info import Statevector
import numpy as np

import weblab.week1

EPSILON = 0.01

zero = Statevector([1, 0])
one = Statevector([0, 1])
plus = Statevector([1 / np.sqrt(2), 1 / np.sqrt(2)])
minus = Statevector([1 / np.sqrt(2), -1 / np.sqrt(2)])
plusi = Statevector([1 / np.sqrt(2), 1j / np.sqrt(2)])
minusi = Statevector([1 / np.sqrt(2), -1j / np.sqrt(2)])

w = weblab.week1

# Solution code
def exercise1(x):
	initial_state = np.sqrt([x,
							 1 - x])  # Create initial state vector. Probability of measuring |0> should be x, hence take the sqrt(x) and sqrt(1-x) to construct the state.
	sv = Statevector(initial_state)  # Create the statevector object using the initial_state.
	return sv  # Return the correct statevector


# Solution code

class TestSolution(unittest.TestCase):
	# def setUp(self):
	#    print(1)

	# Place all the tests between the START comment and the END comment.
	# Do not remove the TESTS comments

	# TESTS START HERE

	def test_ex1_1(self):
		value = 1 / 2
		vector = exercise1(value)
		test_vector = exercise1(value)
		self.assertTrue((np.abs(vector.data) - np.abs(test_vector.data))[0] < EPSILON and
						(np.abs(vector.data) - np.abs(test_vector.data))[1] < EPSILON)

	def test_ex1_2(self):
		value = 0
		vector = exercise1(value)
		test_vector = exercise1(value)
		self.assertTrue((np.abs(vector.data) - np.abs(test_vector.data))[0] < EPSILON and
						(np.abs(vector.data) - np.abs(test_vector.data))[1] < EPSILON)

	def test_ex1_3(self):
		value = 1
		vector = exercise1(value)
		test_vector = exercise1(value)
		self.assertTrue((np.abs(vector.data) - np.abs(test_vector.data))[0] < EPSILON and
						(np.abs(vector.data) - np.abs(test_vector.data))[1] < EPSILON)

	def test_ex1_4(self):
		value = 1 / 3
		vector = exercise1(value)
		test_vector = exercise1(value)
		self.assertTrue((np.abs(vector.data) - np.abs(test_vector.data))[0] < EPSILON and
						(np.abs(vector.data) - np.abs(test_vector.data))[1] < EPSILON)

	def test_ex1_5(self):
		value = 1 / 9.5
		vector = exercise1(value)
		test_vector = exercise1(value)
		self.assertTrue((np.abs(vector.data) - np.abs(test_vector.data))[0] < EPSILON and
						(np.abs(vector.data) - np.abs(test_vector.data))[1] < EPSILON)

	def test_ex2_1(self):
		zero = Statevector([1, 0])
		x, y, z = weblab.week1.exercise2(zero)
		x0, y0, z0 = 0, 0, 1
		distance = np.abs(x - x0) + np.abs(y - y0) + np.abs(z - z0)
		self.assertTrue(distance < EPSILON)

	def test_ex2_2(self):
		one = Statevector([0, 1])
		x, y, z = exercise2(one)
		x1, y1, z1 = 0, 0, -1
		distance = np.abs(x - x1) + np.abs(y - y1) + np.abs(z - z1)
		self.assertTrue(distance < EPSILON)

	def test_ex2_3(self):
		plus = Statevector([1 / np.sqrt(2), 1 / np.sqrt(2)])
		x, y, z = solution.exercise2(plus)
		xplus, yplus, zplus = 1, 0, 0
		distance = np.abs(x - xplus) + np.abs(y - yplus) + np.abs(z - zplus)
		self.assertTrue(distance < EPSILON)

	def test_ex2_4(self):
		minus = Statevector([1 / np.sqrt(2), -1 / np.sqrt(2)])
		x, y, z = solution.exercise2(minus)
		xminus, yminus, zminus = -1, 0, 0
		distance = np.abs(x - xminus) + np.abs(y - yminus) + np.abs(z - zminus)
		self.assertTrue(distance < EPSILON)

	def test_ex2_5(self):
		plusi = Statevector([1 / np.sqrt(2), 1j / np.sqrt(2)])
		x, y, z = solution.exercise2(plusi)
		xplusi, yplusi, zplusi = 0, 1, 0
		distance = np.abs(x - xplusi) + np.abs(y - yplusi) + np.abs(z - zplusi)
		self.assertTrue(distance < EPSILON)

	def test_ex2_6(self):
		minusi = Statevector([1 / np.sqrt(2), -1j / np.sqrt(2)])
		x, y, z = solution.exercise2(minusi)
		xminusi, yminusi, zminusi = 0, -1, 0
		distance = np.abs(x - xminusi) + np.abs(y - yminusi) + np.abs(z - zminusi)
		self.assertTrue(distance < EPSILON)

	def test_ex2_7(self):
		plusplusi = Statevector([1 / np.sqrt(2), np.exp(1j * np.pi / 4) / np.sqrt(2)])
		x, y, z = solution.exercise2(plusplusi)
		xplusplusi, yplusplusi, zplusplusi = 1. / np.sqrt(2), 1. / np.sqrt(2), 0
		distance = np.abs(x - xplusplusi) + np.abs(y - yplusplusi) + np.abs(z - zplusplusi)
		self.assertTrue(distance < EPSILON)

	def test_ex2_8(self):
		zeroC = Statevector([1j, 0])
		x, y, z = solution.exercise2(zeroC)
		x0, y0, z0 = 0, 0, 1
		distance = np.abs(x - x0) + np.abs(y - y0) + np.abs(z - z0)
		self.assertTrue(distance < EPSILON)

	def test_ex3_1(self):
		zeroOrthogonal = solution.exercise3(zero)
		self.assertTrue(zeroOrthogonal.equiv(one))

	def test_ex3_2(self):
		oneOrthogonal = solution.exercise3(one)
		self.assertTrue(oneOrthogonal.equiv(zero))

	def test_ex3_3(self):
		plusOrthogonal = solution.exercise3(plus)
		self.assertTrue(plusOrthogonal.equiv(minus))

	def test_ex3_4(self):
		minusOrthogonal = solution.exercise3(minus)
		self.assertTrue(minusOrthogonal.equiv(plus))

	def test_ex3_5(self):
		plusiOrthogonal = solution.exercise3(plusi)
		self.assertTrue(plusiOrthogonal.equiv(minusi))

	def test_ex3_6(self):
		minusiOrthogonal = solution.exercise3(minusi)
		self.assertTrue(minusiOrthogonal.equiv(plusi))


# TESTS END HERE


if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.TestRunner)