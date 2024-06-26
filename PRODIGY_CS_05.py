from scapy.all import sniff, conf
from scapy.layers.inet import IP, TCP, UDP

# Ensure Scapy uses pcap
conf.use_pcap = True

# Function to process each captured packet
def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n[+] New Packet: {packet.summary()}")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")

        # Check if the packet has a TCP or UDP layer and print the payload
        if packet.haslayer(TCP):
            print("TCP Packet")
            tcp_layer = packet[TCP]
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
            print(f"Payload: {tcp_layer.payload}")

        elif packet.haslayer(UDP):
            print("UDP Packet")
            udp_layer = packet[UDP]
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
            print(f"Payload: {udp_layer.payload}")

        else:
            print("Other Protocol")

# Start sniffing
print("Starting packet sniffer...")
sniff(prn=packet_callback, store=False)
