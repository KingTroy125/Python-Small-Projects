Requirements:
Install the required library:

bash
Copy
pip install python-nmap
Nmap must be installed on your system:

Linux: sudo apt-get install nmap

macOS: brew install nmap

Windows: Download from nmap.org

Usage:
bash
Copy
python nmap_scanner.py <target> [-p <port-range>]
Examples:
Scan default ports (1-1000):

bash
Copy
python nmap_scanner.py 192.168.1.1
Scan specific ports:

bash
Copy
python nmap_scanner.py example.com -p 20-80
Scan single port:

bash
Copy
python nmap_scanner.py 10.0.0.1 -p 443
Notes:
The script shows port numbers, states (open/filtered/closed), and service names

You might need root/sudo privileges to scan certain ports

The scan might take some time depending on the target and port range

Always ensure you have proper authorization before scanning any network

This script provides more detailed output than a simple port scanner, including:

Host status (up/down)

Protocol type (TCP/UDP)

Port state (open/closed/filtered)

Service detection

Remember to use this tool responsibly and only on networks where you have explicit permission to perform scanning.