import numpy as np
import weblabTestRunner
from decorators import *
from qiskit import *

import solution

backendU = Aer.get_backend('unitary_simulator')
EPSILON = 1e-6


class TestSolution(unittest.TestCase):

    @spectest(20)
    def test_implementation_oracle_1(self):
        uf = QuantumCircuit(4)
        uf.cx(0, 2)
        uf.cx(0, 3)

        qc, _ = solution.simonqc(uf)
        qc.remove_final_measurements()

        # undo hadamards
        qc.h(range(2))
        # undo uf
        qc.cx(0, 2)
        qc.cx(0, 3)
        # undo hadamards
        qc.h(range(2))
        # check identity
        unitary = execute(qc, backendU).result().get_unitary()

        process_fidelity = np.abs(np.trace(unitary) / 16) ** 2
        self.assertGreater(process_fidelity, 1 - EPSILON)

    @spectest(20)
    def test_implementation_oracle_2(self):
        uf = QuantumCircuit(4)
        uf.cx(0, 2)
        uf.cx(0, 3)
        uf.cx(1, 2)
        uf.cx(1, 3)

        qc, _ = solution.simonqc(uf)
        qc.remove_final_measurements()

        # undo hadamards
        qc.h(range(2))
        # undo uf
        qc.cx(1, 2)
        qc.cx(1, 3)
        qc.cx(0, 2)
        qc.cx(0, 3)
        # undo hadamards
        qc.h(range(2))

        # check identity
        unitary = execute(qc, backendU).result().get_unitary()
        process_fidelity = np.abs(np.trace(unitary) / 16) ** 2
        self.assertGreater(process_fidelity, 1 - EPSILON)

    @spectest(20)
    def test_implementation_oracle_3(self):
        uf = QuantumCircuit(6)
        uf.cx(0, 3)
        uf.cx(0, 4)
        uf.cx(1, 5)
        qc, _ = solution.simonqc(uf)
        qc.remove_final_measurements()

        # undo hadamards
        qc.h(range(3))
        # undo uf
        qc.cx(0, 3)
        qc.cx(0, 4)
        qc.cx(1, 5)
        # undo hadamards
        qc.h(range(3))
        # check identity
        unitary = execute(qc, backendU).result().get_unitary()

        processFidelity = np.abs(np.trace(unitary) / 64) ** 2
        self.assertGreater(processFidelity, 1 - EPSILON)

    @spectest(10)
    def test_implementation_correctness_1(self):
        uf = QuantumCircuit(4)
        uf.cx(0, 2)
        uf.cx(0, 3)

        _, s = solution.simonqc(uf)

        self.assertEqual(s, [1, 0])

    @spectest(10)
    def test_implementation_correctness_2(self):
        uf = QuantumCircuit(4)
        uf.cx(0, 2)
        uf.cx(0, 3)
        uf.cx(1, 2)
        uf.cx(1, 3)

        _, s = solution.simonqc(uf)

        self.assertEqual(s, [1, 1])

    @spectest(10)
    def test_implementation_correctness_3(self):
        uf = QuantumCircuit(6)
        uf.cx(0, 3)
        uf.cx(0, 4)
        uf.cx(1, 5)

        _, s = solution.simonqc(uf)
        self.assertEqual(s, [1, 0, 0])

    @spectest(10)
    def test_implementation_correctness_4(self):
        uf = QuantumCircuit(6)
        uf.cx(2, 4)
        uf.x(3)
        uf.cx(2, 3)
        uf.ccx(0, 1, 3)
        uf.x(0)
        uf.x(1)
        uf.ccx(0, 1, 3)
        uf.x(0)
        uf.x(1)
        uf.x(3)

        _, s = solution.simonqc(uf)
        self.assertEqual(s, [0, 1, 1])


if __name__ == '__main__':
    unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
