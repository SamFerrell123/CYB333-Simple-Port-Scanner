import socket

# Dictionary mapping port numbers to their names
port_names = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    115: "SFTP",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    194: "IRC",
    443: "SSL",
    445: "SMB",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "Remote Desktop",
    5632: "PCAnywhere",
    5900: "VNC",
    25565: "Minecraft"
}

def port_scan(target, ports):
    open_ports = []
    for port in ports:
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            s.settimeout(1)
            # Attempt to connect to the target IP and port
            result = s.connect_ex((target, port))
            # Check if the port is open
            if result == 0:
                open_ports.append(port)
            # Close the socket
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Port scanning stopped by user.")
            return open_ports
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            return open_ports
        except socket.error:
            print("[!] Couldn't connect to server.")
            return open_ports
    return open_ports

def main():
    print("Welcome to Simple Port Scanner")
    target = input("Enter target IP: ")
    # Define the ports to scan
    ports = list(port_names.keys())
    print(f"Scanning ports for {target}...")
    open_ports = port_scan(target, ports)
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f" - {port}: {port_names[port]}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
