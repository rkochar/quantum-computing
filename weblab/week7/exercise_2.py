from qiskit import *
from library import int2bin, bin2int

backendQ = Aer.get_backend('qasm_simulator')


def simonqc(uf: QuantumCircuit):
    n = uf.num_qubits
    n2 = int(n / 2)
    qc = QuantumCircuit(n)

    # BEGIN SOLUTION
    # Apply Hadamard gates before querying the oracle
    qc.h(range(n2))
    qc.barrier()

    # Apply the query function
    qc = qc + uf
    qc.barrier()

    # Apply Hadamard gates to the top register
    qc.h(range(n2))

    # Measure ancilla qubits
    qc.measure_all()  # use local simulator

    measZ = {}
    while True:
        results = execute(qc, backend=backendQ, shots=n).result()
        answer = results.get_counts()
        # print(answer)

        # Categorize measurements by input register values [cn-1,...,c2,c1,c0]
        for measresult in answer.keys():
            # print(measresult)
            # print(measresult[n2:])
            # for i in measresult[n2:]:
            #    print(i)

            mInt = bin2int([int(i) for i in measresult[n2:]])
            if mInt not in measZ and mInt != 0:
                measZ[mInt] = 1

        if not measZ:
            continue

        answers = []
        for s in range(1, 2 ** (n2)):
            bitS = int2bin(s, n2)
            validSolution = True
            for meas in measZ:
                measS = int2bin(meas, n2)
                # print(measS,bitS)
                # print(measS[0])
                # print(bitS[0])
                pointwiseprod = [measS[i] * bitS[i] for i in range(n2)]
                if sum(pointwiseprod) % 2 == 1:
                    validSolution = False
                    break
            if validSolution:
                answers = answers + [bitS]
        if len(answers) == 1:
            return qc, answers[0]
    return qc
