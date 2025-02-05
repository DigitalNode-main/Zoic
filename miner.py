import ctypes
import json
import hashlib

# Load Pufferfish2 hashing library
pufferfish2 = ctypes.CDLL("./libpufferfish2.so")
pufferfish2.pufferfish2_hash.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

def compute_pufferfish2_hash(data):
    data_bytes = json.dumps(data, sort_keys=True).encode()
    hash_output = ctypes.create_string_buffer(32)
    pufferfish2.pufferfish2_hash(ctypes.c_char_p(data_bytes), hash_output)
    pf2_hash = hash_output.raw.hex()
    return hashlib.sha3_256(pf2_hash.encode()).hexdigest()
