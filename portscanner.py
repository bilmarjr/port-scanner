import socket

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def portscanner(host, scanned_port):
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((host, scanned_port)) == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error scanning port {scanned_port}: {e}")
        return False
    finally:
        s.close()

def main():
    print("Welcome to the Port Scanner!")

    host = input("Enter IP address to scan: ").strip()
    while not validate_ip(host):
        print("Invalid IP address. Try again")
        host = input("Enter IP address to scan: ").strip()

    try:
        start_port = int(input("Enter starting port: ").strip())
        end_port = int(input("Enter ending port: ").strip())

        if start_port<0 or end_port>65535 or start_port>end_port:
            raise ValueError("Invalid port range. Ports must be between 0 and 65535.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"Scanning {host} from port {start_port} to {end_port}...")

    open_ports = []
    for p in range(start_port, end_port+1):
        if portscanner(host, p):
            print(f"Port {p} OPEn")
            open_ports.append(p)
        else:
            print(f"Port {p}: Closed")

    print("\nScan complete!")
    print(f"Open Ports: {open_ports if open_ports else 'None'}")

if __name__ == "__main__":
    main()