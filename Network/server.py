import socket
import json

# Server setup
host = '192.168.1.113'  # Listen on all available interfaces
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connected by {client_address}")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                key_event = json.loads(data.decode('utf-8'))
                print(f"Received: {key_event}")
