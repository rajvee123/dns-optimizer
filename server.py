import socket
import json
from concurrent.futures import ThreadPoolExecutor
from resolver import resolve
from congestion import allow_request
from config import PORT

executor = ThreadPoolExecutor(max_workers=10)


def handle_client(conn, addr):
    data = conn.recv(1024).decode()
    req = json.loads(data)

    domain = req["domain"]
    client_id = req["client_id"]

    if not allow_request(client_id):
        response = {"status": "blocked"}
    else:
        ip = resolve(domain)
        response = {"status": "ok", "ip": ip}

    conn.send(json.dumps(response).encode())
    conn.close()


def start_server():
    server = socket.socket()
    server.bind(("127.0.0.1", PORT))
    server.listen(5)

    print(f"[SERVER RUNNING ON PORT {PORT}]")

    while True:
        conn, addr = server.accept()
        executor.submit(handle_client, conn, addr)
