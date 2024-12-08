import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter IP address to scan: ")
port = int(input("Enter port to scan: "))

def portscanner(scanned_port):
    if s.connect_ex((host, scanned_port)):
        print("The port is closed")
    else:
        print("The port is open")

portscanner(port)