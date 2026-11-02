# LAN File Request Client and Server

A Python TCP socket program that lets a client request and download a file from a server on the same LAN.

## How it works

1. The server listens on TCP port `9999`.
2. The client sends a project-relative file path, such as `exp/3/writeup.md`.
3. The server reads that file and returns its contents.
4. The client saves it in the local `recv-folder` directory.

## Before running

- Install Python 3.
- Connect both devices to the same LAN.
- Allow TCP port `9999` through the server device's firewall.
- On another device, replace `localhost` in `record_client.py` with the server device's IPv4 address.

Find the server IPv4 address from Windows PowerShell:

```powershell
ipconfig
```

Change the client connection line:

```python
c.connect(('SERVER_IP_ADDRESS', 9999))
```

Example:

```python
c.connect(('192.168.1.50', 9999))
```

## Run in Visual Studio Code

### Terminal 1 — server

Open a terminal and move to the project directory:

```powershell
cd d:\Projects\cn_project
python record_server.py
```

Keep this terminal running. It should print:

```text
Socket created
Waiting for connections
```

### Terminal 2 — client

Open a second VS Code terminal with **Terminal → New Terminal**:

```powershell
cd d:\Projects\cn_project
python record_client.py
```

Enter a relative file path when prompted:

```text
exp/3/writeup.md
```

The downloaded file will be saved to:

```text
recv-folder/writeup.md
```

## Run client and server on one computer

In `record_client.py`, use:

```python
c.connect(('localhost', 9999))
```

Start `record_server.py` in Terminal 1 and `record_client.py` in Terminal 2 as shown above.

## Run on two Windows devices

On the server device, Terminal 1:

```powershell
python record_server.py
```

On the client device, Terminal 2:

```powershell
python record_client.py
```

The client device must first use the server's IPv4 address in `record_client.py`.

## Allow the server port in Windows Firewall

Run this once in an Administrator PowerShell:

```powershell
New-NetFirewallRule -DisplayName "Python File Server" -Direction Inbound -Protocol TCP -LocalPort 9999 -Action Allow
```

## Troubleshooting

- `Connection refused`: start the server and verify the configured IP address.
- `File not found`: enter a path relative to the project directory, without a leading `D:\` path.
- Port conflict: stop the previous server process before starting another one.
- Test reachability from another Windows terminal:

```powershell
Test-NetConnection SERVER_IP_ADDRESS -Port 9999
```

`TcpTestSucceeded : True` means the server port is reachable.
