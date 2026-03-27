import socket
import json
import time
import random
from config import PORT, DNS_DB

clients = [
    ("normal", "192.168.1.1"),
    ("normal", "192.168.1.2"),
    ("attacker", "10.0.0.1")
]

domains = list(DNS_DB.keys())


def simulate():
    for _ in range(200):
        s = socket.socket()
        s.connect(("127.0.0.1", PORT))

        client_type, client_ip = random.choice(clients)
        domain = random.choice(domains)

        req = {
            "domain": domain,
            "client_id": client_ip
        }

        s.send(json.dumps(req).encode())
        res = s.recv(1024).decode()

        print(f"[{client_type.upper()}] {domain} -> {res}")

        s.close()

        # attacker is faster
        time.sleep(0.05 if client_type == "attacker" else 0.2)
