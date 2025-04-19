import numpy as np
import random

def braid_operator(theta):
    #this function converts braiding operations as rotation matrix
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

def measure_fusion():
   #this function stimulates the fusion measurement
    return np.random.choice(["vacuum", "non-trivial"], p=[0.9, 0.1])

def topological_bb84(num_qubits=100):
#this function simulates the modified BB84 and also calculate the error rates.

    # Random basis selection
    alice_bases = [random.choice(["Z", "X"]) for _ in range(num_qubits)]
    bob_bases = [random.choice(["Z", "X"]) for _ in range(num_qubits)]

    bob_results = []
    errors = 0
    matching_count = 0

    for i in range(num_qubits):
        state = np.array([1, 0])  # Logical |0⟩_L state

        if alice_bases[i] == "X":
            state = braid_operator(np.pi / 4) @ state  # Alice applies X-basis braiding
        
        if bob_bases[i] == "X":
            state = braid_operator(-np.pi / 4) @ state  # bob applies reverse braiding

        result = measure_fusion()
        bob_results.append(result)

        if alice_bases[i] == bob_bases[i]:  # Counting only matching bases
            matching_count += 1
            if result == "non-trivial":
                errors += 1

    error_rate = errors / matching_count if matching_count > 0 else 0

    return {
        "Matching Basis Pairs": matching_count,
        "Errors Detected": errors,
        "Final Secret Key Length": matching_count - errors,
        "Error Rate": error_rate*100
    }
#changing the number of qubits to 500
simulation_results = topological_bb84(500)
print(simulation_results)
