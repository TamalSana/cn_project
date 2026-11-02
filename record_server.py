import socket
import os

s = socket.socket()
print("Socket created")

s.bind(('0.0.0.0', 9999))
s.listen(3)
print("Waiting for connections")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    c, addr = s.accept()
    print("Connected with", addr)

    requested_file = c.recv(1024).decode('utf-8').strip().replace('\\', '/')
    file_path = os.path.join(BASE_DIR, requested_file)

    try:
        with open(file_path, 'rb') as file:
            c.sendall(file.read())
    except FileNotFoundError:
        c.sendall(b"ERROR: File not found")

    c.close()
