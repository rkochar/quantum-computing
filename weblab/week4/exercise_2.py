import numpy as np
from qiskit import *
from exercise_2_library import *

def exercise2(f, n, m):
    q = QuantumRegister(n + m)
    qc = QuantumCircuit(q)
    matrix = np.zeros((2 ** (n + m), 2 ** (n + m)))
    ### BEGIN SOLUTION
    # Iterate over the entire input space
    for x in range(2 ** n):
        # Get output for input
        fx = f(int2bin(x, n))
        # Convert to binary list
        fxInt = bin2int(fx)
        for y in range(2 ** m):
            # Calculate the output register
            outReg = (y + fxInt) % (2 ** m)
            # Get corresponding row
            row = outReg * 2 ** n + x
            # Get corresponding column
            col = y * 2 ** n + x
            # Set output in index to 'high' as it is output
            matrix[row][col] = 1
    # Convert the element to a unitary and apply to the circuit.
    qc.unitary(matrix, q)
    ### END SOLUTION
    return qc
