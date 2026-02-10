import numpy as np
import random

# Quantum states (Z and X bases)
H = np.array([[1], [0]])
V = np.array([[0], [1]])
PLUS = (1 / np.sqrt(2)) * (H + V)
MINUS = (1 / np.sqrt(2)) * (H - V)

# Alice prepares a random qubit state


def alice_choose():
    basis = random.choice(['Z', 'X'])
    bit = random.choice([0, 1])
    if basis == 'Z':
        state = H if bit == 0 else V
    else:
        state = PLUS if bit == 0 else MINUS
    return basis, bit, state

# Bob measures the qubit in a random basis using Born's rule


def bob_measure(state, basis):
    if basis == 'Z':
        measurement_basis = [H, V]
    else:
        measurement_basis = [PLUS, MINUS]

    probs = []
    for b in measurement_basis:
        inner = (b.T.conj() @ state)[0, 0]
        p = np.abs(inner) ** 2
        probs.append(p)

    probs = np.array(probs, dtype=float)
    probs /= np.sum(probs)

    result = np.random.choice([0, 1], p=probs)
    return int(result)