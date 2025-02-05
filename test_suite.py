import unittest
from wallet import QuantumResistantWallet
from miner import compute_pufferfish2_hash

class TestZoiClassic(unittest.TestCase):
    def test_generate_wallet(self):
        wallet = QuantumResistantWallet.generate_wallet()
        self.assertTrue("address" in wallet)

    def test_pufferfish2_hash(self):
        data = {"test": "block"}
        self.assertEqual(len(compute_pufferfish2_hash(data)), 64)

if __name__ == "__main__":
    unittest.main()
