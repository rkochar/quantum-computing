import numpy as np
from qiskit.quantum_info import Statevector


def exercise1(x):
    initial_state = np.sqrt([x,
                             1 - x])  # Create initial state vector. Probability of measuring |0> should be x, hence take the sqrt(x) and sqrt(1-x) to construct the state.
    sv = Statevector(initial_state)  # Create the statevector object using the initial_state.
    return sv  # Return the correct statevector


def exercise2(statevector):
    # get the coefficients of |0> and |1>
    coef0 = statevector.data[0]
    coef1 = statevector.data[1]
    EPSILON = 1e-6

    """
    Solution without trig
    """
    a = np.sqrt(np.real(coef0 * coef0.conjugate()))
    if abs(a) < EPSILON:
        b = 1
    else:
        b = coef0.conjugate() * coef1 / a

    br = b.real
    bi = b.imag

    z = 2 * a ** 2 - 1
    x = 2 * a * br
    y = 2 * a * bi

    return [x, y, z]

    """
    Solution with trig
    """
    # compute theta based on the angular representation of state vector. |phi> = cos(theta/2)|0> + e^i*phi sin(theta/2)|1>
    theta = 2 * np.arccos(coef0)
    # if theta is 0 then alpha can't be computed.
    if theta < 0.001:
        return [0, 0, 1]
    alpha = coef1 / np.sin(theta / 2.0)  # alpha = (cos(phi) + isin(phi))
    if np.real(alpha) + 1.0 < 0.001:
        phi = np.pi
    else:
        phi = 2 * np.arctan(np.imag(alpha) / (np.real(alpha) + 1))

    return [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)]


def exercise3(statevector):
    # get the coefficients of |0> and |1>
    coef0 = statevector.data[0]
    coef1 = statevector.data[1]
    # compute theta based on the angular representation of state vector. |phi> = cos(theta/2)|0> + e^i*phi sin(theta/2)|1>
    theta = 2 * np.arccos(coef0)
    # if statevector is [1,0] then orthogonal is [0,1].
    if theta < 0.001:
        return Statevector([0, 1])
    alpha = coef1 / np.sin(theta / 2.0)  # alpha = (cos(phi) + isin(phi))
    if np.real(alpha) + 1.0 < 0.001:
        phi = np.pi
    else:
        phi = 2 * np.arctan(np.imag(alpha) / (np.real(alpha) + 1))
    a = np.cos((theta - np.pi) / 2.0)
    b = (np.cos(phi) + 1.0j * np.sin(phi)) * np.sin((theta - np.pi) / 2.0)
    return Statevector([a, b])


#
import unittest

EPSILON = 0.01


class TestSolution(unittest.TestCase):
    # Place all the tests between the START comment and the END comment.
    # Do not remove the TESTS comments
    # Feel free to add your own tests

    # TESTS START HERE

    def test_ex1_1(self):
        vector = exercise1(0.5)
        test_vector = Statevector([1 / np.sqrt(2), 1 / np.sqrt(2)])
        self.assertTrue(vector.equiv(test_vector, atol=EPSILON))

    def test_ex2_1(self):
        zero = Statevector([1, 0])
        x, y, z = exercise2(zero)
        x0, y0, z0 = 0, 0, 1
        distance = np.abs(x - x0) + np.abs(y - y0) + np.abs(z - z0)
        self.assertTrue(distance < EPSILON)

    def test_ex3_1(self):
        zero = Statevector([1, 0])
        one = Statevector([0, 1])
        zeroOrthogonal = exercise3(zero)
        self.assertTrue(zeroOrthogonal.equiv(one))

    def test(self):
        pos = Statevector([1 / 2 ** 2, np.exp(np.pi / 3) / 2 ** 2])
        x, y, z = exercise2(pos)
        print("x: ", x, "y: ", y, "z: ", z)
        self.assertTrue(True)


# TESTS END HERE

if __name__ == "__main__":
    unittest.main(TestSolution)
