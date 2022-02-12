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
    def test_student(self):
        n = 1
        qc = QuantumCircuit(n)
        # prepare state correponding to y=1: |0>-|1>
        qc.x(0)
        qc.h(0)
        qc = qc + solution.transformation(n)

        out = Statevector(execute(qc, backend).result().get_statevector())
        assert out.equiv(Statevector(np.array([0, 1]))), out

    @spectest(10)
    def test_assert_phase(self):
        n = 1
        qc = QuantumCircuit(n)
        # prepare state correponding to y=0: |0>-|1>
        qc.h(0)
        qc = qc + solution.transformation(n)

        out = Statevector(execute(qc, backend).result().get_statevector())
        self.assertTrue(out.equiv(Statevector(np.array([1, 0]))), out)

    @parameterized([PTC(y, name=f"Test with input {y}", weight=2)
                    for y in range(2 ** 5)])
    def test_parameterized_partial(self, y):
        n = 5
        qc = QuantumCircuit(n)
        # prepare state correponding to y
        ybitstr = format(y, '0' + str(n) + 'b')
        for i in range(n):
            if ybitstr[-(i + 1)] == '1':
                qc.x(i)
            qc.h(i)
        qc = qc + solution.transformation(n)

        out = Statevector(execute(qc, backend).result().get_statevector())
        target = np.zeros(2 ** n)
        target[y] = 1
        self.assertTrue(out.equiv(target))


if __name__ == '__main__':
    unittest.main(testRunner=weblabTestRunner.WeightedTestRunner)
