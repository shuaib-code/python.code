import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Server IP address: {local_ip}")
