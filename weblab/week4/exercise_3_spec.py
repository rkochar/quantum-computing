import unittest
from qiskit import *
from qiskit.circuit.library import CXGate, CCXGate
import solution
import numpy as np
import weblabTestRunner
from decorators import *

backend = Aer.get_backend('unitary_simulator')
validGates = (CXGate, CCXGate)
EPSILON = 1e-6


class TestSolution(unittest.TestCase):
    # Place all the tests between the START comment and the END comment.
    # Do not remove the TESTS comments
    # Feel free to add your own tests

    # TESTS START HERE
    @spectest(5)
    @required_spectest(100)
    def test_valid_gates(self):
        qc = solution.exercise3()
        for g in qc.data:  # Check type of gates used
            self.assertTrue(isinstance(g[0], validGates), g[0])

    @spectest(35)
    def test_circuit_validity(self):
        qc = solution.exercise3()
        matrix = np.matrix(
            [[1. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j],
             [0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 1. + 0.j],
             [0. + 0.j, 0. + 0.j, 1. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j],
             [0. + 0.j, 1. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j],
             [0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 1. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j],
             [0. + 0.j, 0. + 0.j, 0. + 0.j, 1. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j],
             [0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 1. + 0.j, 0. + 0.j],
             [0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, 1. + 0.j, 0. + 0.j, 0. + 0.j]])

        qc.unitary(matrix.T, qc.qregs[0])

        job = execute(qc, backend)
        unitary = job.result().get_unitary(qc, decimals=8)
        processFidelity = np.abs(np.trace(unitary) / 8) ** 2
        self.assertGreater(processFidelity, 1 - EPSILON)


# TESTS END HERE

if __name__ == "__main__":
    unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
