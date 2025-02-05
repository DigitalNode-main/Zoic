import socket
import threading
import json
from zoic_blockchain import blockchain

class StratumMiningPool:
    def __init__(self, host='0.0.0.0', port=3333):
        self.host = host
        self.port = port

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Stratum mining pool running on port {self.port}")
        while True:
            client_socket, _ = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            response = json.dumps(blockchain.generate_mining_job())
            client_socket.send(response.encode())
        client_socket.close()

if __name__ == "__main__":
    mining_pool = StratumMiningPool()
    mining_pool.start()
