import hashlib
import base58
from pqcrypto.sign import dilithium5  # Post-Quantum Lattice-based Signatures

class QuantumResistantWallet:
    @staticmethod
    def generate_wallet():
        sk, pk = dilithium5.generate_keypair()
        address = base58.b58encode(hashlib.sha3_256(pk).digest()).decode()
        return {
            "address": address,
            "public_key": pk.hex(),
            "private_key": sk.hex()
        }
