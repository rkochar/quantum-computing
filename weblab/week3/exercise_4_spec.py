import unittest
from qiskit import *
from qiskit.circuit.library import CXGate, RZGate
import solution
import numpy as np
import weblabTestRunner
from decorators import spectest, required_spectest

backend = Aer.get_backend('unitary_simulator')
validGates = (CXGate, RZGate)
EPSILON = 1e-6

class TestSolution(unittest.TestCase):
# Place all the tests between the START comment and the END comment.
# Do not remove the TESTS comments
# Feel free to add your own tests

# TESTS START HERE

    @spectest(4)
    @required_spectest(100)
    def test_correct_gateset(self):
        qc = solution.exercise4()

        for g in qc.data:  # Check type of gates used
            assert isinstance(g[0], validGates), g[0]

    @spectest(5)
    def test_correctness(self):
        qc = solution.exercise4()

        qc.cp(-np.pi / 8, 1, 0)
        qc.x(0)
        qc.cp(np.pi / 8, 1, 0)
        qc.x(0)

        job = execute(qc, backend)
        unitary = job.result().get_unitary(qc, decimals=8)
        processFidelity = np.abs(np.trace(unitary) / 4) ** 2
        self.assertGreater(processFidelity, 1 - EPSILON)

    @spectest(1)
    def test_minimal_gateset(self):
        qc = solution.exercise4()

        for g in qc.data:  # Check type of gates used
            assert isinstance(g[0], validGates), g[0]

        self.assertEquals(len(qc.data), 4)
# TESTS END HERE


if __name__ == "__main__":
    unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)