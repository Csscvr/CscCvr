import socket

def check_open_ports(ip_address, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # set timeout to 1 second
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            print(f"Error connecting to port {port}")
    return open_ports

ip_address = input("Enter the IP address to scan: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

open_ports = check_open_ports(ip_address, start_port, end_port)

if open_ports:
    print(f"Open ports on {ip_address}: {', '.join(map(str, open_ports))}")
else:
    print(f"No open ports found on {ip_address} in the range {start_port}-{end_port}")