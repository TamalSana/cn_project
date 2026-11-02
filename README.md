# LAN File Request Client and Server

A Python TCP socket program that lets a client request and download a file from a server on the same LAN. 
Each lab sub-directory has: i)writeup(.html) ii)cpt project file(.cpt) {binary format}

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
exp/1/lab1.pkt
```

The downloaded file will be saved to:

```text
recv-folder
```

## Run client and server on one computer

In `record_client.py`, use:

```python
c.connect(('localhost', 9999))
```

## Test: Client and server on PC + wsl:

```python
c.connect(('server device ip', 9999))
```



