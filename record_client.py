import socket
import os

c = socket.socket()
c.connect(('localhost', 9999))

requested_file = input("Enter record path (for example exp/3/writeup.md): ").strip().replace('\\', '/')
c.send(requested_file.encode('utf-8'))

received_data = bytearray()
while True:
    chunk = c.recv(65536)
    if not chunk:
        break
    received_data.extend(chunk)

c.close()

output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recv-folder")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, os.path.basename(requested_file))

with open(output_path, 'wb') as file:
    file.write(received_data)

print("Saved received file to", output_path)
