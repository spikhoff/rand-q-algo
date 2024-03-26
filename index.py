from qiskit import QuantumCircuit, Aer, execute
import hashlib

class QuantumBlock:
    def __init__(self, data):
        self.data = data
        self.previous_hash = None
        self.hash = None
        self.qc = self.create_quantum_circuit()

    def create_quantum_circuit(self):
        # Create a quantum circuit representing the data
        qc = QuantumCircuit(len(self.data), 1)
        for i, bit in enumerate(self.data):
            if bit == '1':
                qc.x(i)
        return qc

    def mine(self, difficulty):
        # Mine the block by finding a hash with required difficulty
        target = '0' * difficulty
        nonce = 0
        while True:
            self.qc.reset(0)
            self.qc.measure(0, 0)
            backend = Aer.get_backend('qasm_simulator')
            job = execute(self.qc, backend, shots=1)
            result = job.result()
            counts = result.get_counts()
            output_hash = hashlib.sha256(str(counts).encode()).hexdigest()
            if output_hash.startswith(target):
                self.hash = output_hash
                break
            nonce += 1
        print("Block mined with nonce:", nonce)

class QuantumBlockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 4  # Difficulty for PoW

    def add_block(self, data):
        if len(self.chain) > 0:
            previous_hash = self.chain[-1].hash
        else:
            previous_hash = None
        new_block = QuantumBlock(data)
        new_block.previous_hash = previous_hash
        new_block.mine(self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print("Data:", block.data)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)
            print()

# Example usage
if __name__ == "__main__":
    blockchain = QuantumBlockchain()
    blockchain.add_block("Hello, quantum world!")
    blockchain.add_block("Quantum computing rocks!")
    blockchain.print_chain()
