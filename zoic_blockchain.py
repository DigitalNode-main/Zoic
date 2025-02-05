import hashlib
import json
import threading
from decimal import Decimal

class ZoiClassicBlockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.utxo = {}
        self.peers = set()
        self.create_genesis_block()
        self.mining_jobs = {}

    def create_genesis_block(self):
        genesis_block = {"index": 0, "previous_hash": "0", "transactions": [], "merkle_root": "0"}
        self.chain.append(genesis_block)

blockchain = ZoiClassicBlockchain()
