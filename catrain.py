print("ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos, Queen >⩊<"); 

from scapy.all import IP, TCP, ICMP, send # type: ignore // pip install scapy --python C:\path\to\python

target_ip = input("IP: ")
count = input("Count: ")
packetT = IP(dst=target_ip) / TCP(flags="S")
packetI = IP(dst=target_ip) / ICMP()

sent_count = 0
for i in range(count):
    send(packetT)
    send(packetI)
    sent_count += 1
    print(f"Sent packet {sent_count} to IP {target_ip}")
input("All sent~~")
