from qiskit import *
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import HGate, CPhaseGate, Barrier
from qiskit.circuit import Instruction

validGates = (HGate, CPhaseGate, Barrier)
import solution
import numpy as np
import weblabTestRunner
from decorators import *

backend = Aer.get_backend('statevector_simulator')
zeroTwoQubits = np.kron([1, 0], [1, 0])
zeroFourQubits = np.kron(zeroTwoQubits, zeroTwoQubits)
zeroSixQubits = np.kron(zeroFourQubits, zeroTwoQubits)
zeroEightQubits = np.kron(zeroSixQubits, zeroTwoQubits)
zeroTenQubits = np.kron(zeroEightQubits, zeroTwoQubits)


def check(gate, validGates):
	"""
	Recursive helper function that checks whether circuits only make use
	of the allowed gate sets.
	"""
	if isinstance(gate, validGates):
		return True
	elif isinstance(gate, Instruction):
		for g in gate.definition.data:
			if not check(g[0], validGates):
				break
		else:
			# Only occurs when break is not executed.
			return True
	return False


class TestSolution(unittest.TestCase):
	# Place all the tests between the START comment and the END comment.
	# Do not remove the SPECTESTS comments

	# SPECTESTS START HERE

	@spectest(10)
	def test_size2(self):
		n = 2
		qc = solution.sumqft(n)
		qc = qc.inverse()
		qc.x(1)
		qc.x(2)
		qc = qc.inverse()
		# We want to add 1=(01) with 2=(10)

		# We remove 1=(01) from the top register and 3=(11) from the bottom
		qc.x(1)
		qc.x(2)
		qc.x(3)

		out = Statevector(execute(qc, backend).result().get_statevector())

		self.assertTrue(out.equiv(Statevector(zeroFourQubits)))

	@spectest(10)
	def test_size3(self):
		n = 3
		qc = solution.sumqft(n)
		qc = qc.inverse()
		qc.x(1)
		qc.x(2)
		qc.x(4)
		# We want to add 6=(110) with 2=(010)
		qc = qc.inverse()
		# We remove 1=(01) from the top register and 3=(11) from the bottom
		qc.x(1)
		qc.x(2)

		out = Statevector(execute(qc, backend).result().get_statevector())

		self.assertTrue(out.equiv(Statevector(zeroSixQubits)))

	@spectest(20)
	def test_size4(self):
		n = 4
		qc = solution.sumqft(n)
		qc = qc.inverse()
		qc.x(1)
		qc.x(2)
		qc.x(4)
		# We want to add 6=(0110) with 1=(0001)
		qc = qc.inverse()

		qc.x(1)
		qc.x(2)
		qc.x(4)
		qc.x(5)
		qc.x(6)

		out = Statevector(execute(qc, backend).result().get_statevector())

		self.assertTrue(out.equiv(Statevector(zeroEightQubits)))

	@spectest(20)
	def test_size5(self):
		n = 5
		qc = solution.sumqft(n)
		qc = qc.inverse()
		qc.x(1)
		qc.x(2)
		qc.x(4)
		# We want to add 22=(10110) with 0=(0000)
		qc = qc.inverse()

		qc.x(1)
		qc.x(2)
		qc.x(4)
		qc.x(6)
		qc.x(7)
		qc.x(9)

		out = Statevector(execute(qc, backend).result().get_statevector())

		self.assertTrue(out.equiv(Statevector(zeroTenQubits)))

	@required_spectest(100)
	@spectest(20)
	def testGates(self):
		for n in range(1, 10):
			qc = solution.sumqft(n)
			for g in qc.data:  # Check type of gates used
				self.assertTrue(check(g[0], validGates))


# SPECTESTS END HERE


if __name__ == "__main__":
	unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)