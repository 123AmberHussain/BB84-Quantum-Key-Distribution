# main.py
import bb84_core

def main():
    print("--- Quantum Key Distribution (BB84) Simulator ---")
    try:
        num_trials = int(input("How many trials do you want to run? "))
        photons_per_trial = int(input("How many photons per trial? "))
        target_key_length = 8
        
        # We call the core logic here
        bb84_core.run_trials(num_trials, photons_per_trial, target_key_length)
        
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == '__main__':
    main()