from qiskit.quantum_info import Statevector
import numpy as np
from qiskit import *


def exercise1(state):
	"""
    Alternative solution using equiv (provided by Dr. Elkouss).
    # Unroll the different parameters

    alpha00, alpha01, alpha10, alpha11 = state.data
    # Find general expression of the combined state in terms of two qubits
    state0 = Statevector(np.array([alpha00, alpha01] / np.sqrt(abs(alpha00) ** 2 + abs(alpha01) ** 2)))
    state1 = Statevector(np.array([alpha10, alpha11] / np.sqrt(abs(alpha10) ** 2 + abs(alpha11) ** 2)))
    # If these two states are not equivalent, then we cannot decompose the state with common
    # terms. Hence the qubits must be entangled.
    return not (state0.equiv(state1))
    """
	# Define error margin
	EPSILON = 1e-6
	# Unrol the different parameters of input state
	a, b, c, d = state.data
	# Determine the degree of entanglement
	return abs(a * d - b * c) > EPSILON
