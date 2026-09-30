
from scapy.all import sniff, IP, TCP, UDP, ICMP, ARP
from collections import defaultdict
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from time import time

console = Console()

stats = defaultdict(int)
connections = defaultdict(list)
alerts = set()
total = 0

def make_dashboard():
    table = Table(title="NETWORK SNIFFER DASHBOARD")
    table.add_column("Metric", style="cyan")
    table.add_column("Count", justify="right", style="green")

    table.add_row("Total Packets", str(total))
    table.add_row("TCP", str(stats["TCP"]))
    table.add_row("UDP", str(stats["UDP"]))
    table.add_row("ICMP", str(stats["ICMP"]))
    table.add_row("ARP", str(stats["ARP"]))
    table.add_row("Other", str(stats["OTHER"]))
    table.add_row("Security Alerts", str(len(alerts)))

    return Panel(table, subtitle="Live Monitoring")

def capture_packet(packet):
    global total

    total += 1

    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
            tcp = packet[TCP]

            if tcp.flags & 0x02 and not tcp.flags & 0x10:
                now = time()
                connections[src] = [
                    t for t in connections[src]
                    if now - t < 10
                ]
                connections[src].append(now)

                if len(connections[src]) >= 10:
                    if src not in alerts:
                        alerts.add(src)
                        console.print(
                            f"[red]Possible port scan: {src}[/red]"
                        )

        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "OTHER"

        stats[protocol] += 1

    elif ARP in packet:
        stats["ARP"] += 1

with Live(make_dashboard(), refresh_per_second=2) as live:
    def update(packet):
        capture_packet(packet)
        live.update(make_dashboard())

    try:
        print("Starting Network Sniffer...")
        sniff(prn=update, store=False)
    except KeyboardInterrupt:
        print("Sniffer stopped.")
