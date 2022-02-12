from qiskit import QuantumCircuit
import numpy as np


def modifieddj(uf):
    n = uf.num_qubits - 1
    djCircuit = QuantumCircuit(n + 1)

    # BEGIN SOLUTION

    # Since all qubits are initialized to |0>, we need to flip the second register qubit to the |1> state
    djCircuit.x(n)

    # Apply Hadamard gates to all qubits
    djCircuit.h(range(n + 1))

    # Query the oracle
    djCircuit = djCircuit + uf

    # Transform case 1 to constant f and case 2 to balanced f
    djCircuit.cx(0, n)

    # Apply Hadamard gates to all gates
    djCircuit.h(range(n + 1))

    # Undo flip on second register to go back to all zeros for case 1
    djCircuit.x(n)
    return djCircuit
