# 🔐 Network Sniffer

A Python-based network sniffer built using **Scapy** to capture, monitor and analyze network packets in real time. It provides protocol analysis, basic suspicious activity detection and a live terminal dashboard.

## 🚀 Features

* **Live Packet Capture:** Capture network packets in real time.
* **Protocol Analysis:** Identify TCP, UDP, ICMP and ARP packets.
* **IP Address Monitoring:** Display source and destination IP addresses.
* **Port Analysis:** Inspect TCP and UDP source and destination ports.
* **Protocol Filtering:** Capture specific protocols such as TCP, UDP, ICMP and ARP.
* **PCAP Export:** Save captured packets for further analysis in Wireshark.
* **Basic Security Alerts:** Identify unusual TCP SYN activity that may indicate a port scan.
* **Live Dashboard:** Monitor packet counts and security alerts in the terminal.

## 🛠️ Tech Stack

* **Language:** Python
* **Packet Capture:** Scapy
* **Packet Analysis:** TCP/IP
* **Terminal Dashboard:** Rich
* **Packet Inspection:** Wireshark, tcpdump
* **Operating System:** Kali Linux

## 📋 Prerequisites

* Kali Linux or another compatible Linux distribution
* Python 3
* Git
* Root privileges for packet capture

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/utkarshc06/Network-Sniffer.git
```

**2. Navigate to the project directory**

```bash
cd Network-Sniffer
```

**3. Install dependencies**

```bash
sudo apt update
sudo apt install python3-scapy python3-rich tcpdump -y
```

## ▶️ Usage

**1. Start the network sniffer**

```bash
sudo python3 sniffer.py
```

**2. Generate network traffic**

Open another terminal and run:

```bash
ping -c 10 8.8.8.8
```

**3. Stop the sniffer**

Press `Ctrl + C` to stop packet capture.

## 📡 Protocol Filtering

The earlier command-line version of the sniffer supports the following filters:

| Protocol | Command                                   |
| -------- | ----------------------------------------- |
| TCP      | `sudo python3 sniffer.py --protocol tcp`  |
| UDP      | `sudo python3 sniffer.py --protocol udp`  |
| ICMP     | `sudo python3 sniffer.py --protocol icmp` |
| ARP      | `sudo python3 sniffer.py --protocol arp`  |
| All      | `sudo python3 sniffer.py --protocol all`  |

## 💾 Saving Packets

The PCAP-enabled version supports saving captured packets for offline analysis.

```bash
sudo python3 sniffer.py --protocol icmp --count 20 --output capture.pcap
```

Read the captured packets using:

```bash
tcpdump -r capture.pcap
```

You can also open the PCAP file in Wireshark.

**Note:** The protocol-filtering and PCAP commands refer to the earlier versions of the script. The final dashboard version does not yet combine these features.

## 🛡️ Security Detection

The basic detection module monitors repeated TCP SYN packets from the same source IP within a short time window.

It generates an alert when the configured threshold is reached.

Example:

```text
[ALERT] Possible port scan from 192.168.1.105
```

This is a basic heuristic. It may produce false positives and is not a replacement for a full intrusion detection system.

## 📊 Dashboard

The terminal dashboard provides:

* Total captured packets
* TCP packet count
* UDP packet count
* ICMP packet count
* ARP packet count
* Other packet count
* Number of security alerts

## 📁 Project Structure

```text
Network-Sniffer/
│
├── sniffer.py
├── README.md
└── capture.pcap    # Generated during capture
```

## 🎯 Learning Outcomes

* Understanding TCP/IP networking
* Learning live packet capture with Scapy
* Analyzing network protocols and IP addresses
* Working with PCAP files
* Understanding TCP SYN traffic
* Implementing basic network anomaly detection
* Building terminal-based monitoring dashboards

## 🔒 Ethical Use

This project is intended for educational purposes and authorized network monitoring only. Capture traffic only on networks and devices for which you have permission. Avoid collecting or sharing sensitive packet data.

---

**⭐ If you find this project useful, consider giving the repository a star.**
