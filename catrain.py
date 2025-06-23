from argparse import ArgumentParser as AP

print("ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos' Queen >ω<")

import subprocess as s; from sys import exit as sexit

try:
	if b"scapy" not in s.check_output("pip list", shell=True):
		print("Scapy not installed... Installing for u :3 (will exit the script after -m-)"); s.call("pip install scapy", shell=True); sexit()
except Exception as e: input(f"Scapy installation failed: {e}. Please install manually using 'pip install scapy'"); sexit()

from argparse import ArgumentParser as AP

def get_args():
	parser = AP(description="ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos' Queen >ω<", prog="CATRAIN", epilog="Created by Queen of Lmaos for testing network infrastructure uwuh~")
	parser.add_argument("-i", "--ip", type=str, help="Target IP address")
	parser.add_argument("-c", "--count", type=int, help="Packet run count (3 packets per run)")
	parser.add_argument("-s", "--srcip", type=str, help="Source IP. Default: '192.168.1.2'\nNote that if --mac == 'y'; there is no default and format is 12:90:ad:F3:7c:Eb", default="192.168.1.2")
	parser.add_argument("-t", "--threadcount", type=int, help="Thread count")
	parser.add_argument("-f", "--interface", type=str, help="The name of the interface to use.\nDefaults: 'eth0' on Linux; first Ethernet interface on Windows IF --mac == 'y'. Else uses system default.")
	parser.add_argument("-p", "--showping", type=str, choices=['y', 'n'], help="Show ping (y/n)", default="y")
	parser.add_argument("-e", "--hidethreads", type=str, choices=['y', 'n'], help="Hide most threads from showing in UI. Recommended for 20+ threads (y/n)", default="n")
	parser.add_argument("-d", "--data", type=str, help="The data to be sent. No more than 1456 chars. Is repeated and cut off to fill up 1456 chars (default: 'HI! :3 ')")
	parser.add_argument("-r", "--randomsrc", type=str, choices=['y', 'n'], help="Randomize the source IP or MAC. (y/n)", default="n")
	parser.add_argument("-n", "--delay", type=str, help="Add a delay between packets and/or packet runs, in seconds. Format: PACKET_DELAY:RUN_DELAY\nUse a colon ':' to specify which number is which as such;\n[-n PACKET_DELAY:] [-n PACKET_DELAY] [-n :RUN_DELAY] [-n PACKET_DELAY:RUN_DELAY]")
	parser.add_argument("-m", "--mac", type=str, choices=['y', 'n'], help="In stead of an ip, target a mac address. [using ip field] (Disables pinging) (y/n)", default="n")
	parser.add_argument("--debug", type=bool, help="Enable debug output [show errors, stop UI resets, output settings on start]", default=False)
	parser.add_argument("--verbose", type=bool, help="Enable packet logs", default=False)
	parser.add_argument("--exit", type=bool, help="Exit immediately on completion", default=False)
	return parser.parse_args()

from re import match as rmatch, search as research; from os import name as osname

try:
	args = get_args() # setting variables to their either default values or requested values in input/args based on various arguments
	if not args.ip or args.count is None or args.threadcount is None:
		target_ip = args.ip if args.ip else input("\t\t\t    MAC: ") if args.mac and not args.ip and args.randomsrc != 'y' else input("\t\t\t      IP: ") if args.randomsrc != 'y' else ''
		count = args.count if args.count is not None else int(input("Packet run count (3 packets per): "))
		threadcount = args.threadcount if args.threadcount > 2 else int(input("\t\t    Thread count: "))
		if threadcount > 2: raise ValueError("Thread count has to be 2 or more.")
	else: target_ip, count, threadcount = args.ip, args.count, args.threadcount
	if args.srcip: srcIp = args.srcip

	if args.interface: interface_name=args.interface
	elif args.mac == 'y': # set interface based on input and/or os type
		if osname=="nt":
			interface_name = research(r"Ethernet adapter \w+^\:", s.check_output("ipconfig", shell=True)).group().trim().removeprefix("Ethernet adapter ")
			if not interface_name: raise ValueError("Missing Ethernet adapter. Set an interface.")
		else: interface_name = "eth0"
	else: interface_name = None

	if args.showping: showp = args.showping
	if args.hidethreads: hideThreads = args.hidethreads
	data = bytes(args.data, 'utf-8')*(int(1456/len(args.data))) if args.data else b"HI! :3 "*208 # set data to a series of the input or default, filling up 1456 bytes as much as possible
		#! Eth MTU size = 1500, -44 for TCP blocks == 1456 ;; divide by length
	if args.randomsrc: randIp = args.randomsrc
	if args.mac: macMode = args.mac
	debugMode = args.debug; verbose = args.verbose
	exitation = args.exit

	packet_delay = int(args.delay.split(':')[0]) if args.delay and ':' in args.delay else packet_delay = int(args.delay) if args.delay else 0
	run_delay    = int(args.delay.split(':')[1]) if args.delay and ':' in args.delay else run_delay = 0

	if macMode == "y" and not rmatch(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", target_ip) and randIp != 'y': raise ValueError("Invalid MAC address") # these check for valid targets
	if macMode == "n" and not rmatch(r"^(?:25[0-5]|2[0-4]\d|1?\d{1,2})(?:\.(?:25[0-5]|2[0-4]\d|1?\d{1,2})){3}$", target_ip) and randIp != 'y': raise ValueError("Invalid IPV4 address")
except Exception as e: print(f"\nError: {str(e)}. Type more carefully ffs."); sexit()

if debugMode: # print out debug text - settings/variables
	print(
f"""Settings:
Target:\t\t{research(r"0+", ('-' + target_ip).zfill(20)).group(0).replace('0', ' ') + target_ip}\tCount and Thread count: {count}, {threadcount}
Packets per run:\t\t  3 \tProjection:\t\t{3*count*threadcount}
Pinging:\t\t      {" True" if showp == 'y' else False}\tHiding threads: \t{True if hideThreads == 'y' else False}
Source:\t\t{research(r"0+", ('-' + srcIp).zfill(20)).group(0).replace('0', ' ') + srcIp if randIp != 'y' else 'Randomized'}
Interface: {research(r"0+", ('-' + interface_name).zfill(25)).group(0).replace('0', ' ') + interface_name if interface_name else "System Default"}
MAC mode:\t\t      {" True" if macMode else False}
{'='*70}
Debug mode:\t\t       Duh.\tExit on completion: {exitation}
Verbose output: \t      {" True" if verbose else False}
{'='*70}
Data (repeated {int(1456/len(args.data)) if args.data else 208} - {len(data)} bytes):\t{args.data if args.data else 'HI! :3 '}""")

rno = [True] * threadcount; rcount = [0] * threadcount

# ScaPy config mostly to stop it from doing a lot of stuff thats just not needed
from scapy.all import Raw, conf

if not verbose:
	conf.verb = False
else: conf.verb = True
conf.resolve = False; conf.stealth = 1

conf.route_autoload = False
conf.route6_autoload = False

if interface_name: conf.iface = interface_name


if macMode == "n":
	from scapy.all import IP, TCP, ICMP, UDP, send, fuzz
	if randIp == "n":
		def scr(number):
			try:
				packetI = IP(dst=target_ip, src=srcIp) / ICMP() / Raw(load=data)
				packetT = IP(dst=target_ip, src=srcIp) / fuzz(TCP(flags='S')) / Raw(load=data)
				packetU = IP(dst=target_ip, src=srcIp) / fuzz(UDP()) / Raw(load=data)
				for i in range(count):
					send(packetI); sleep(packet_delay); send(packetT); sleep(packet_delay); send(packetU); sleep(packet_delay)
					sleep(run_delay)
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
					send(packetT); sleep(packet_delay); send(packetI); sleep(packet_delay); send(packetU); sleep(packet_delay)
					sleep(run_delay)
					rcount[number] += 1
			except Exception as e: print(e) if debugMode else 0
			rno[number] = False
else:
	from scapy.all import ARP, Ether, sendp
	if randIp == "n":
		def scr(number):
			try:
				packetA = Ether(dst=target_ip, src=srcIp, type=0x0806) / ARP(hwsrc=srcIp, psrc="255.255.255.255", hwdst=target_ip, pdst="127.0.0.1") / Raw(load=data) # ARP
				packetE = Ether(dst=target_ip, src=srcIp, type=0x88B5) / Raw(load=data) # Custom/EtherCAT
				packetC = Ether(dst=target_ip, src=srcIp, type=0x88B6) / Raw(load=data) # Custom
				for i in range(count):
					sendp(packetA); sleep(packet_delay);sendp(packetE); sleep(packet_delay); sendp(packetC); sleep(packet_delay)
					sleep(run_delay)
					rcount[number] += 1
			except Exception as e: print(e) if debugMode else 0
			rno[number] = False
	else:
		from random import randint as r
		def scr(number):
			temp = [r(0x00, 0xff) for i in range(6)]; temp[0] &= 0xfe # Multicast bit = 0
			src = ":".join("%02x" % b for b in temp)
			try:
				packetA = Ether(dst=target_ip, src=src, type=0x0806) / ARP(hwsrc=src, psrc="255.255.255.255", hwdst=target_ip, pdst="127.0.0.1") / Raw(load=data) # ARP
				packetE = Ether(dst=target_ip, src=src, type=0x88B5) / Raw(load=data) # Custom/EtherCAT
				packetC = Ether(dst=target_ip, src=src, type=0x88B6) / Raw(load=data) # Custom
				for i in range(count):
					sendp(packetA); sleep(packet_delay); sendp(packetE); sleep(packet_delay); sendp(packetC); sleep(packet_delay)
					sleep(run_delay)
					rcount[number] += 1
			except Exception as e: print(e) if debugMode else 0
			rno[number] = False

from threading import Thread; from time import sleep, time

starttime=time()

threads = []
for x in range(threadcount):
	t = Thread(target=scr, args=(x,)); t.start()
	threads.append(t); print(f"called sub {x+1}")


while any(rno):
	status_lines = ["ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos' Queen >ω<", "THR no. | Running\t| Packets sent\t| Packet run no.", "—" * 56 ]
	try:
		sleep(0.5)
		elt = int(research(r"\d+", str(time()-starttime)).group(0))

		if hideThreads == "n" or threadcount == 1:
			for i in range(0, threadcount, 1): status_lines.append(f"{i+1}.\t| {rno[i]}\t\t| {str(rcount[max(i, 1)]*3).zfill(8)}\t| {str(rcount[i]).zfill(8)}")
		else:
			for i in range(0, max(1, min(int(threadcount/10+0.9), 10)), 1): status_lines.append(f"{i+1}.\t| {rno[i]}\t\t| {str(rcount[max(i, 1)]*3).zfill(8)}\t| {str(rcount[i]).zfill(8)}")
		if macMode == 'y': status_lines.append(f"\nTarget MAC: {target_ip if randIp != 'y' else "Randomized"}  ")
		else: status_lines.append(f"\nTarget IP: {target_ip if randIp != 'y' else "Randomized"}")
		status_lines.append(f"Source {'IP' if macMode == 'n' else 'MAC'}: {srcIp if randIp == "n" else "Randomized "}    {"\t" if not macMode else ''}\tTotal estimated packets: {rcount[int(len(rcount)/2+0.9)]*3*threadcount}")
		if hideThreads == "y": status_lines.append(f"Time: {int((elt-(elt%(60**2)))/(60*60))}h {int((elt-(elt%60))/60)}min {elt%60}s\t\t\tTotal threads: {threadcount}")
		else: status_lines.append(f"Time: {int((elt-(elt%(60**2)))/(60*60))}h {int((elt-(elt%60))/60)}min {elt%60}s")
		status_lines.append(f"Completion: {str(research(r"\d+[\.,](?:\d\d\d|\d\d|\d)", str((rcount[int(len(rcount)/2+0.9)]/count)*100)).group(0))}%\t\t\tData: {"HI! :3 " if not args.data else f"'{args.data}'"}")

		if not debugMode:
			if osname == "nt": s.call("cls", shell=True)
			else: s.call("clear", shell=True)

		print("\n".join(status_lines)+"\n")
	except Exception as e: print(e) if debugMode else 0

input("All sent~~") if not exitation else print("All sent~~")
