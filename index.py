from qiskit import QuantumCircuit, Aer, execute

# Define a quantum circuit
qc = QuantumCircuit(2, 1)

# Apply Hadamard gate to the first qubit
qc.h(0)

# Apply controlled-NOT gate with the first qubit as control and the second qubit as target
qc.cx(0, 1)

# Measure the second qubit
qc.measure(1, 0)

# Simulate the quantum circuit
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1000)
result = job.result()
counts = result.get_counts()

# Display measurement results
print("Measurement results:", counts)
