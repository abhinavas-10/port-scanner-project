🔍 Simple Python Port Scanner
📌 Overview

This project is a simple command-line Port Scanner built using Python. It allows users to scan a target IP address or domain and identify open ports within a specified range.

🚀 Features
🌐 Scan any IP address or domain (e.g., 127.0.0.1, localhost)
🔢 Custom port range selection
⚡ Detects open ports quickly
🕒 Displays scan start and end time
🖥️ Simple CLI-based interface
🛠️ Technologies Used
Python 🐍
Socket Programming
Datetime module
📂 Project Structure
PortScannerProject/
│── port_scanner.py
│── README.md
⚙️ How It Works
User enters:
Target IP / domain
Start port
End port
Script scans each port using sockets
Displays open ports
▶️ Usage

Run the script using:

python port_scanner.py

Example input:

Enter target IP or domain: 127.0.0.1
Enter start port: 1
Enter end port: 1024

Example output:

[+] Port 135 is OPEN
[+] Port 445 is OPEN
📸 Output Preview
=== Simple Python Port Scanner ===
Scanning target: 127.0.0.1
Port range: 1 - 1024

[+] Port 135 is OPEN
[+] Port 445 is OPEN
📊 Key Concepts Used
TCP Socket connection
Exception handling
Network basics (Ports & Protocols)
<img width="949" height="535" alt="Screenshot 2025-12-06 205007" src="https://github.com/user-attachments/assets/26daad3d-54bf-46d9-8515-d328d195be3f" />
