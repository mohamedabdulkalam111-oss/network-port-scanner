
import socket
import ipaddress
from datetime import datetime

# Common port-to-service mappings
SERVICES = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP Alternative"
}


def scan_port(target, port):
    """Check whether a TCP port accepts a connection."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            return result == 0
    except OSError:
        return False


def main():
    print("=" * 45)
    print("       NETWORK PORT SCANNER")
    print("=" * 45)

    target = input("Enter target IP address: ").strip()

    # Validate the IP address
    try:
        ipaddress.ip_address(target)
    except ValueError:
        print("Error: Please enter a valid IP address.")
        return 1

    # Get and validate the port range
    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))
    except ValueError:
        print("Error: Ports must be whole numbers.")
        return 1

    if not (1 <= start_port <= end_port <= 65535):
        print("Error: Enter ports from 1 to 65535,")
        print("and ensure the starting port is not greater than the ending port.")
        return 1

    print(f"\nTarget: {target}")
    print(f"Port range: {start_port}-{end_port}")
    print("-" * 45)

    # Prepare the report
    report = [
        "NETWORK PORT SCANNER REPORT",
        f"Target IP: {target}",
        f"Scan date: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"Port range: {start_port}-{end_port}",
        "-" * 45
    ]

    open_count = 0

    # Scan the selected ports
    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            service = SERVICES.get(port, "Unknown service")
            message = f"Port {port}: OPEN | Service: {service}"
            print(message)
            report.append(message)
            open_count += 1

    if open_count == 0:
        message = "No open ports found in this range."
        print(message)
        report.append(message)

    report.append("-" * 45)
    report.append(f"Open ports found: {open_count}")
    report.append("Scan completed!")

    # Save the report
    try:
        with open("scan_report.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(report) + "\n")
        print("\nScan completed!")
        print("Report saved to scan_report.txt")
    except OSError as error:
        print(f"Error saving report: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
