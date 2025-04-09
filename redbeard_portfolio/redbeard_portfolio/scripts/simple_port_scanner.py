import socket

def scan_ports(target, ports):
    print(f"🔍 Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((target, port))
            print(f"✅ Port {port} is OPEN")
            sock.close()
        except:
            pass

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    port_range = range(20, 1025)
    scan_ports(target_ip, port_range)
