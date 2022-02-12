from qiskit import *
from qiskit.circuit.library import CXGate, CCXGate
from qiskit.quantum_info import Statevector

import solution
import numpy as np
import weblabTestRunner
from decorators import *

backend = Aer.get_backend('statevector_simulator')
validGates = (CXGate, CCXGate)
EPSILON = 1e-6


class TestSolution(unittest.TestCase):

    @spectest(10)
    def test_case(self):
        uf = QuantumCircuit(4)
        # create a, constant given x_0, circuit
        uf.cx(0, 3)
        dj = solution.modifieddj(uf)

        out = Statevector(execute(dj, backend).result().get_statevector())

        self.assertTrue(out.equiv(Statevector(
            np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))))

    @spectest(15)
    def test_hidden(self):
        uf = QuantumCircuit(4)
        # create a circuit implementing f with number of zeros when x_0=0 + number of ones when x_0=1 equal 2^{n-1}
        uf.cx(1, 3)
        dj = solution.modifieddj(uf)

        out = execute(dj, backend).result().get_statevector()
        self.assertGreater(EPSILON, np.abs(out[0]))


if __name__ == '__main__':
    unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
