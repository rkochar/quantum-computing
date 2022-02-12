from qiskit import QuantumCircuit, QuantumRegister
from numpy import pi


def qft_rotations(circuit, n):
    if n == 0: # Exit function if circuit is empty
        return circuit
    n -= 1 # Indexes start from 0
    circuit.h(n) # Apply the H-gate to the most significant qubit
    for qubit in range(n):
        # For each less significant qubit, we need to do a
        # smaller-angled controlled rotation:
        circuit.cp(pi/2**(n-qubit), qubit, n)
    qft_rotations(circuit, n)

def sumqft(n):
  qc = QuantumCircuit(2*n)
  qftn = QuantumCircuit(n)
  qft_rotations(qftn,n)
  qc.append(qftn,qc.qregs[0][n:2*n])

  for i in range(n):
    for j in range(n-i):
      # rotation from y_i (position i) to x_j  (position n+j) qubit
      # This would be the textbook rotation, but we have not done the swaps!
      # Hence, the qubit at 2n-1 is the qubit at n, 2n-2 is the qubit at n+1:
      qc.cp(pi/2**(n-i-j-1), i, 2*n-1-j)
  qc.append(qftn.inverse(),qc.qregs[0][n:2*n])
  return qc