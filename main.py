from qiskit import *
import numpy as np
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi
from qiskit.quantum_info import Statevector

def draw():
    q = QuantumRegister(2)
    qc = QuantumCircuit(q)

    qc.initialize([1 / sqrt(2), 1j / sqrt(2)], 0)
    qc.initialize([0, 1], 1)
    qc.barrier()

    qc.h(1)
    qc.cx(1, 0)
    qc.rz(np.pi / 3, 0)
    print(qc)


def tutorial1():
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)

    # qc.initialize([1, 0], 0)
    # qc.initialize([0, 1], 1)
    qc.initialize([-sqrt(2)/sqrt(3), 1/(sqrt(3))], 0)
    # qc.initialize([1 / sqrt(2), -1j / sqrt(2)], 1)
    qc.barrier()
    qc.x(q)
    qc.rx(np.pi/3, q)
    qc.y(q)

    qc.barrier()
    qc.h(q)
    qc.rz(np.pi/3, q)
    qc.h(q)

    # qc.barrier()
    qc.z(q)





    # Other question
    # qc.t(0)
    # qc.cz(0, 1)

    print(qc)
    qc.draw()

    result = Aer.get_backend('statevector_simulator').run(assemble(qc)).result()
    out_state = result.get_statevector()
    print("tut: ", out_state)
    return out_state

def check():
    q = QuantumRegister(1)
    qc = QuantumCircuit(q)

    # qc.initialize([1, 0], 0)
    # qc.initialize([0, 1], 1)
    qc.initialize([-sqrt(2) / sqrt(3), 1 / (sqrt(3))], 0)
    # qc.initialize([1 / sqrt(2), -1j / sqrt(2)], 1)
   # a
    qc.barrier()
    qc.y(q)
    # qc.cx(0, 1)
    # qc.t(0)
    # qc.h(1)

    # b
    # qc.cz(0, 1)
    # qc.t(0)
    # qc.t(1)

    # c is correct
    # qc.h(1)
    # qc.cx(0, 1)
    # qc.t(0)
    # qc.h(1)

    # d
    # qc.h(1)
    # qc.cx(0, 1)
    # qc.t(0)

    print(qc)
    qc.draw()

    result = Aer.get_backend('statevector_simulator').run(assemble(qc)).result()
    out_state = result.get_statevector()
    print("check: ", out_state)
    return out_state


def tutorial():
    qc = QuantumCircuit(1)  # Create a quantum circuit with one qubit
    initial_state = [0, 1]  # Define initial_state as |1>
    qc.initialize(initial_state, 0)  # Apply initialisation operation to the 0th qubit
    qc.draw()  # Let's view our circuit
    svsim = Aer.get_backend('statevector_simulator')  # Tell Qiskit how to simulate our circuit
    qobj = assemble(qc)  # Create a Qobj from the circuit for the simulator to run
    result = svsim.run(qobj).result()  # Do the simulation and return the result
    out_state = result.get_statevector()
    print(out_state)  # Display the output state vector

def own_cx(qc, control, target):
    """
    Implement cx by compiling CZ sandwiched by 2 hadamard gates.
    """
    qc.h(target)
    qc.cp(np.pi, control, target)
    qc.h(target)

def own_swap(qc, idx1, idx2):
    """
    Implement swap with 3 cx's.
    """
    own_cx(qc, idx1, idx2)
    own_cx(qc, idx2, idx1)
    own_cx(qc, idx1, idx2)

if __name__ == '__main__':
    # draw()
    t = tutorial1()
    c = check()

    # print(t)
    print('----------------------------------------------------')
    # print(c)
    print(t == c)

