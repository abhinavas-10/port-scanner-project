import socket
from datetime import datetime

def scan_port(target_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # avoid long waits
    try:
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
    except:
        pass
    finally:
        s.close()

if __name__ == "__main__":
    print("=== Simple Python Port Scanner ===")
    target = input("Enter target IP or domain (e.g. 127.0.0.1 / localhost): ")
    start_port = int(input("Enter start port (e.g. 1): "))
    end_port = int(input("Enter end port (e.g. 1024): "))

    print(f"\nScanning target: {target}")
    print(f"Port range: {start_port} - {end_port}")
    print("Scan started at:", datetime.now())
    print("------------------------------------")

    # Resolve domain to IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: Could not resolve hostname.")
        exit()

    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

    print("------------------------------------")
    print("Scan finished at:", datetime.now())
