Live URL:   https://aminbiography.github.io/port-scanner/



<h1>Project Overview: Port Scanner</h1>
A port scanner is a tool that checks for open ports on a machine. Open ports can sometimes expose vulnerabilities in the system, so it’s important to identify them to understand the security posture of a system.

<h2>Prerequisites:</h2>
Basic knowledge of Python programming.
A Linux environment (any Linux distribution will work).
Basic understanding of networking (IP addresses, ports, and protocols).

<h2>Steps:</h2>
01. Set up Python on Linux: Ensure that Python is installed on your Linux system. You can check this by running the command:

python3 --version

If not installed, you can install Python using:

sudo apt update
sudo apt install python3


02. Understand Socket Programming: In this project, you will use Python’s socket library to interact with the network.
   
03. Create the Port Scanner Script:  

## Port Scanner

This project is a simple **Port Scanner** implemented in Python. It scans a given IP address to identify open ports within a specified range.

### Code Python

```
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

```



<h1>How the Script Works:</h1>

Socket: The socket library is used to create a connection attempt to each port. The connect_ex() function returns 0 if the connection is successful (i.e., the port is open).

Threading: Since scanning a range of ports can take a long time, threading is used to scan multiple ports simultaneously.

Timeout: The timeout is set to 1 second for each connection attempt, which is configurable.

<h1>How to Run:</h1>

01. Save the script as port_scanner.py
2. Open a terminal and navigate to the directory where the script is saved.
3. Run the script with:

python3 port_scanner.py

04. Provide an IP address and port range when prompted.

<h1>Things to Experiment With:</h1>

Scan Specific Ports: Modify the script to scan for a specific list of ports, such as common ports like 80 (HTTP), 443 (HTTPS), 21 (FTP), etc.

Scan for Multiple IPs: Expand the script to scan a list of IPs for vulnerabilities.

Service Detection: Once an open port is found, use the socket.getservbyport() function to try to detect the service running on that port.

<h1>Security Considerations:</h1>

Use with Permission: Always remember to get permission before scanning someone else’s network or systems. Unauthorized port scanning can be considered illegal in many jurisdictions.

Firewall Testing: You can also test how firewalls block your attempts to connect to certain ports.

<p>This simple project will help you get started with coding, networking, and understanding basic cybersecurity concepts.</p>


