import socket
import threading

# Function to check if a port is open
def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Timeout after 1 second
    result = sock.connect_ex((ip, port))  # Returns 0 if the connection is successful
    if result == 0:
        print(f"Port {port} is OPEN")
    sock.close()

# Function to scan ports within a given range
def scan_ports(ip, start_port, end_port):
    print(f"Scanning IP: {ip}")
    threads = []
    for port in range(start_port, end_port+1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()  # Wait for all threads to complete

# Main function
if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    scan_ports(target_ip, start_port, end_port)
