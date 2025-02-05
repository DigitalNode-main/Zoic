from flask import Flask, jsonify, request
from wallet import QuantumResistantWallet
from zoic_blockchain import blockchain

app = Flask(__name__)

@app.route('/generate_wallet', methods=['GET'])
def generate_wallet():
    wallet = QuantumResistantWallet.generate_wallet()
    return jsonify(wallet)

@app.route('/get_blockchain', methods=['GET'])
def get_blockchain():
    return jsonify(blockchain.chain)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
