from qiskit import *
from qiskit.quantum_info import Statevector

import solution
import numpy as np
import weblabTestRunner
from decorators import *

backend = Aer.get_backend('statevector_simulator')

backendU = Aer.get_backend('unitary_simulator')
EPSILON = 1e-6


class TestSolution(unittest.TestCase):

	@spectest(10)
	def test_s1(self):
		s = 1
		r1 = solution.rotate(s)
		qc = QuantumCircuit(r1.qregs[0])

		qc.h(0)
		qc.h(1)
		qc = qc + r1

		out = Statevector(execute(qc, backend).result().get_statevector())
		self.assertTrue(out.equiv(Statevector(np.array([1, 1, 1, -1]) / 2)))

	@spectest(10)
	def test_s2(self):
		s = 2
		q2 = solution.rotate(s)
		q2.cx(2, 0)
		q2.h(2)
		q2 = q2.inverse()

		out = Statevector(execute(q2, backend).result().get_statevector())
		self.assertTrue(out.equiv(Statevector(np.array([1, 0, 0, 0, 0, -1j, 0, 0]) / np.sqrt(2))))


if __name__ == '__main__':
	unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
