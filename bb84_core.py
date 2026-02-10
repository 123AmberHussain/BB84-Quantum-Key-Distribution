import numpy as np
import pandas as pd
import random
import os
import quantum_utils as q_u


# BB84 protocol: send fixed number of photons, then compare bases
def bb84_fixed_photons(num_photons):
    alice_bits = []
    alice_bases = []
    bob_bases = []
    bob_results = []

    for _ in range(num_photons):
        a_basis, a_bit, photon = q_u.alice_choose()
        b_basis = random.choice(['Z', 'X'])
        b_bit = q_u.bob_measure(photon, b_basis)

        alice_bits.append(a_bit)
        alice_bases.append(a_basis)
        bob_bases.append(b_basis)
        bob_results.append(b_bit)

    # Compare bases after all photons are sent
    alice_key = []
    bob_key = []
    for i in range(num_photons):
        if alice_bases[i] == bob_bases[i]:
            alice_key.append(alice_bits[i])
            bob_key.append(bob_results[i])

    return alice_key, bob_key

# Run multiple trials and save keys to CSV


def run_trials(num_trials, photons_per_trial, target_key_length):
    data = []
    trial_id = 1

    for _ in range(num_trials):
        a_key, b_key = bb84_fixed_photons(photons_per_trial)

        if len(a_key) >= target_key_length:
            key_str = ''.join(map(str, a_key[:target_key_length]))
            data.append([trial_id, key_str])
            trial_id += 1
        else:
            trial_id += 1

    if data:
        df = pd.DataFrame(data, columns=["Trial Number", "Key"])
        df["Key"] = df["Key"].astype(str)
        
        # --- FIXED FOR DATA FOLDER ---
        if not os.path.exists('data'):
            os.makedirs('data')
        filename = os.path.join('data', "bb84_keys.csv")
        # -----------------------------
        
        try:
            if os.path.exists(filename):
                os.remove(filename)
            df.to_csv(filename, index=False)
            print(f"\n{len(data)} valid trials saved to '{filename}'.")
        except PermissionError:
            print(f"\nPermission denied: please close '{filename}' and try again.")
    else:
        print("\nNo valid keys generated.")
