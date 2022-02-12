import numpy as np
import weblabTestRunner
from decorators import *
from qiskit import *
from qiskit.extensions import UnitaryGate, Barrier

import library
import solution

backendU = Aer.get_backend('unitary_simulator')
EPSILON = 1e-6


class TestSolution(unittest.TestCase):

    @spectest(10)
    @required_spectest(100)
    def test_valid_circuit(self):
        for x in range(1, 9):
            qc = solution.qft(x)
            gates = list(filter(lambda gate: not isinstance(gate, Barrier), qc.data))
            self.assertEqual(len(gates), 1)
            self.assertTrue(isinstance(gates[0][0], UnitaryGate))

    @parameterized([PTC(n, weight=5, name=f"Running for size {n}") for n in range(1, 9)])
    def test_parameterized_execution(self, n):
        qftbook = library.qft_test(n)

        qc = solution.qft(n)
        qftbook.unitary(qc.data[0][0].inverse(), range(n))

        job = execute(qftbook, backendU)
        unitary = job.result().get_unitary(qftbook, decimals=8)

        processFidelity = np.abs(np.trace(unitary) / 2 ** n) ** 2
        self.assertGreater(processFidelity, 1 - EPSILON)


if __name__ == '__main__':
    unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
