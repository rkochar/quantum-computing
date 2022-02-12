import unittest
from qiskit.quantum_info import Statevector
from qiskit import *
import solution
import numpy as np
import weblabTestRunner
from decorators import PTC, parameterized


class TestSolution(unittest.TestCase):

	# Place all the tests between the START comment and the END comment.
	# Do not remove the TESTS comments

	# TESTS START HERE

	@parameterized([PTC(Statevector(np.array([1, 0, 0, 0])), weight=5, name="Asymetric case |00>"),
					PTC(Statevector(np.array([0, 0, 0 - 1j, 0])), weight=5, name="Asymetric case -i|10>"),
					PTC(Statevector(np.array([0, (1 + 1j) / np.sqrt(2), 0, 0])), weight=5, name="Asymetric case |01>")])
	def test_unentangled(self, vector):
		entangled = solution.exercise1(vector)
		self.assertFalse(entangled)

	@parameterized([
		PTC(Statevector(np.array([1., 0., 0., 1.]) / np.sqrt(2.)), True, True, weight=5, name="Test phi plus state"),
		PTC(Statevector(np.array([1., 1., 1., 1.]) / 2.), False, False, weight=5, name="Test plus plus state"),
		PTC(Statevector(np.array([1., 0., 0., -1.]) / np.sqrt(2.)), True, True, weight=5, name="Test phi minus state"),
		PTC(Statevector(np.array([1., -1., 1., -1.]) / 2.), False, False, weight=5, name="Test plus minus state"),
		PTC(Statevector(np.array([1., -1., -1., -1.]) / 2.), True, False, weight=5,
			name="Test other entangled state (1)"),
		PTC(Statevector(np.array([-1., 1., 1., -1.]) / 2.), False, False, weight=5,
			name="Test other untangled state (2)")
	])
	def test_parameterized(self, vector, asserted, absolute, last=True):
		entangled = solution.exercise1(vector)
		self.assertEqual(entangled, asserted)
		sneaky_test_1 = Statevector(np.abs(vector.data))
		self.assertEqual(solution.exercise1(sneaky_test_1), absolute,
						 "The entanglement should change depending on absolute")
		sneaky_test_2 = Statevector(np.abs(vector.data))
		sneaky_test_2.data[0] *= -1
		self.assertEqual(solution.exercise1(sneaky_test_2), last,
						 "Every chosen test state should be entangled with this setup")


# TESTS END HERE


if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
