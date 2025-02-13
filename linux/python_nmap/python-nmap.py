import nmap
import argparse

def main(target, ports):
    # Initialize the PortScanner
    nm = nmap.PortScanner()
    
    # Perform the scan
    print(f"Scanning {target} on ports {ports}...")
    nm.scan(target, ports)
    
    # Check if the scan was successful
    if not nm.all_hosts():
        print("No hosts found or target is unreachable.")
        return
    
    # Iterate through scan results
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        
        # Iterate through all protocols (tcp, udp, etc.)
        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")
            
            # Get list of ports
            list_ports = nm[host][proto].keys()
            
            # Print header
            print(f"PORT\tSTATE\tSERVICE")
            
            # Iterate through each port
            for port in list_ports:
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                print(f"{port}/{proto}\t{state}\t{service}")

if __name__ == "__main__":
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description='Simple Nmap Scanner')
    parser.add_argument('target', help='Target IP address or hostname')
    parser.add_argument('-p', '--ports', 
                        help='Port range to scan (default: 1-1000)',
                        default='1-1000')
    args = parser.parse_args()
    
    main(args.target, args.ports)