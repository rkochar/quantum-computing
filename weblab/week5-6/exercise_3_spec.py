from qiskit import *
from qiskit.quantum_info import Statevector

import solution
import numpy as np
import weblabTestRunner
from decorators import *

backend = Aer.get_backend('statevector_simulator')
EPSILON = 1e-6


class TestSolution(unittest.TestCase):

    @spectest(10)
    def test_nand_gate(self):
        n = 2
        uf = QuantumCircuit(n + 1)
        uf.ccx(0, 1, 2)
        uf.x(2)

        po = solution.phase_oracle(uf, n, np.pi)

        qc = QuantumCircuit(n + 1)
        qc.h(0)
        qc.h(1)

        out = Statevector(execute(qc + po, backend).result().get_statevector())
        self.assertTrue(out.equiv(Statevector(
            np.array([-1, -1, -1, 1, 0, 0, 0, 0]) / np.sqrt(4))))

    @spectest(10)
    def test_and_gate(self):
        n = 2
        uf = QuantumCircuit(n + 1)
        uf.ccx(0, 1, 2)

        po = solution.phase_oracle(uf, n, np.pi)

        qc = QuantumCircuit(n + 1)
        qc.h(0)
        qc.h(1)

        out = Statevector(execute(qc + po, backend).result().get_statevector())
        self.assertTrue(out.equiv(Statevector(
            np.array([1, 1, 1, -1, 0, 0, 0, 0]) / np.sqrt(4))))

    @parameterized(
        [PTC(np.pi / 5, Statevector(np.array([*[np.exp(1j * np.pi / 5)] * 3, 1, 0, 0, 0, 0]) / np.sqrt(4)), "nand",
             name="Test pi/5 phase", weight=5),
         PTC(np.pi / 23, Statevector(np.array([1, 1, 1, np.exp(1j * np.pi / 23), 0, 0, 0, 0]) / np.sqrt(4)), "and",
             name="Test pi/23 phase", weight=5)
         ])
    def test_arbitrary_rotation(self, phase: np.float64, outcome: Statevector, oracle: str):
        n = 2
        uf = QuantumCircuit(n + 1)

        if oracle == "nand":
            uf.ccx(0, 1, 2)
            uf.x(2)
        elif oracle == "and":
            uf.ccx(0, 1, 2)

        po = solution.phase_oracle(uf, n, phase)

        qc = QuantumCircuit(n + 1)
        qc.h(0)
        qc.h(1)

        out = Statevector(execute(qc + po, backend).result().get_statevector())
        self.assertTrue(out.equiv(outcome))


if __name__ == '__main__':
    unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
