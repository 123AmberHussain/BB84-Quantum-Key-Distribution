**BB84 Quantum Key Distribution Simulator:**
A Python-based simulation of the BB84 Protocol. This project simulates the exchange of polarized photons between Alice and Bob to establish a secure cryptographic key using the principles of quantum mechanics.

**Features**
Modular Architecture: Separates quantum logic, protocol execution, and user interface.

Born's Rule Implementation: Simulates Bob's measurements based on quantum probability.

Sifting Process: Automatically compares Alice and Bob's bases to extract a shared secret key.

Data Persistence: Successful keys are exported to CSV for further analysis.

**Project Structure**
main.py: The entry point for the simulation.

bb84_core.py: Contains the protocol logic and trial management.

quantum_utils.py: The "physics engine" defining states (H, V, PLUS, MINUS) and measurement logic.

data/: Stores generated cryptographic keys.

**Installation & Usage**
- Clone the repository:

Bash
git clone https://github.com/123AmberHussain/BB84-Quantum-Key-Distribution.git
cd BB84-Quantum-Key-Distribution

- Install requirements:

Bash
pip install -r requirements.txt

- Run the simulation:

Bash
python main.py

**How it Works**
The simulation follows the standard BB84 stages:

Preparation: Alice chooses a random bit and a random basis (Rectilinear or Diagonal) to prepare a photon state.

Measurement: Bob chooses a random basis to measure the incoming photon.

Sifting: Alice and Bob publicly announce their bases. They keep bits where their bases matched and discard the rest.

Key Extraction: The remaining bits form the final secure key.
