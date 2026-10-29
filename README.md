
# Network Port Scanner

## About
A beginner-friendly cybersecurity project built with Python.
It scans a specified TCP port range on an authorized target,
identifies common services by port number, and saves the results
to a text report.

## Features
- Validates IPv4 and IPv6 addresses
- Scans a user-defined TCP port range
- Detects ports that accept TCP connections
- Displays common service names
- Saves results in `scan_report.txt`
- Handles invalid IP addresses, port numbers, and file errors

## Technologies Used
- Python 3
- Socket programming
- IP address validation
- Linux / Ubuntu

## Requirements
- Python 3 installed
- Ubuntu, Linux, macOS, or another Python-compatible system

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python3 scanner.py
   ```

4. Enter the target IP address.
5. Enter the starting and ending ports.
6. Review the results in the terminal and `scan_report.txt`.

## Example

```text
Enter target IP address: 127.0.0.1
Enter starting port: 20
Enter ending port: 100

Target: 127.0.0.1
Port range: 20-100
Port 22: OPEN | Service: SSH

Scan completed!
Report saved to scan_report.txt
```

*Actual results depend on which services are running on the target.*

## Project Structure

```text
network-port-scanner/
├── scanner.py
├── README.md
└── scan_report.txt  # Generated after a scan
```

## Learning Outcomes
- Python functions, loops, and conditional statements
- TCP sockets and connection testing
- IP address and port-range validation
- Exception handling and file operations
- Basic network security concepts

## Safety and Disclaimer
Use this tool only on your own computer or on systems for
which you have explicit permission to test. An open port does
not automatically indicate a security vulnerability.

## Future Improvements
- Export reports to CSV
- Add automated unit tests
- Improve port status and error reporting
