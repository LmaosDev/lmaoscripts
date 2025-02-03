import subprocess, re; from os import name as os_name; from sys import path; ppath = path;

#? written in py 3.12.6, most likely wont work before 3.9.x/3.10.x

print("IPV4 only. This version only supports one wildcard or range at a time. RANGES ONLY WORK ON THE LAST TWO NUMBERS. Edit to work with more iuw, and submit to https://github.com/LmaosDev/lmaoscripts/tree/pingprober\n") 
print(f"OS = {os_name}\n") 
ip = input("Provide an ip address:\t (Format: (xxx/*).(xxx/*).(xxx/*/x-x).(xxx/*/x-x) / localhost(:xxxx)/::xxxx )\n > ") 
name = input("Name of scan-file: {Skippable with Enter} [Provide a full path to save in a specific directory] > ")
ip_list = []; reslist = []; sm_24 = True 

# test if ip is parsable/usable
if re.match('(?:(?:\d+|\*)\.(?:\d+|\*)\.(?:(?:\d|\*)+|\d+\-\d+)\.(?:(?:\d|\*)+|\d+\-\d+)|localhost\:*\d*|\:\:\d+)', ip)!=None: # type: ignore 
    input('\nProvided IP is applicable.\nContinue with provided IP?\n\t^C to cancel > ') 
else: input('\nPwovidwed ip wiww nowt wowk umu\n\tre.match: None'); exit() 

#for '*' in ip:
if '*' in ip:
    for i in range(255):
        ip_list.append(f'{ip.replace("*", str(i+1))}') 
elif '-' in ip:
    ip_split = ip.split('-')[0].split('.') 
    try: ip_split += ip.split('-')[1].split('.') 
    except Exception as e: print('parsing failure: ', e) 
    
    input("Split IP :: "+str(ip_split)+'\n^C to cancel > ') 
    
    if ip.split('-')[0].count('.') == 2:
        sm_24 = False 
    
    if sm_24 == True:
        ip_main = ip_split[0]+'.'+ip_split[1]+'.'+ip_split[2] 
        print('Major IP: ' + ip_main + '.0/24') 

        if ip_split[3] <= ip_split[4]:
            ip_start = int(ip_split[3]); ip_end = int(ip_split[4]) 
        else: ip_start = int(ip_split[4]); ip_end = int(ip_split[3]) 
        print(f'start ip: {ip_main + '.' + str(ip_start)}\t end ip: {ip_main + '.' + str(ip_end)}') 

        for i in range(ip_end-ip_start+1): 
            ip_list.append(f'{ip_main}.{str(ip_start + i)}') 

    else: #! sm = /16 /// x.x.x-x.x/16 
        ip_main = ip_split[0]+'.'+ip_split[1] 
        print('Major IP: ' + ip_main + '.0.0/16') 

        if ip_split[2] <= ip_split[3]:
            ip_start = int(ip_split[2]); ip_end = int(ip_split[3]) 
        else: ip_start = int(ip_split[3]); ip_end = int(ip_split[2]) 
        print(f'start ip: {ip_main + '.' + str(ip_start)}.{ip_split[4]}\t end ip: {ip_main + '.' + str(ip_end)}.{ip_split[4]}') 

        for i in range(ip_end-ip_start+1): 
            ip_list.append((f'{ip_main}.{str(ip_start + i)}.{ip_split[4]}')) 
    
else: ip_list.append(ip) 

c = 0 
print('IPs:', ip_list); input("\nCancel? ^C > ") 
if os_name == "posix":
    for x in ip_list:
        try: tempstr = subprocess.check_output(f"ping {x} -c 4", shell=True).decode() 
        except Exception as e: tempstr = f"ping -c 4 {ip_list[c]} failed: {e}" 
        reslist.append(tempstr) 
        print(f"{ip_list[c]}\n{reslist[c]}") 
        c += 1 
else: 
    for x in ip_list:
        try: tempstr = subprocess.check_output(f"ping {x}", shell=True).decode() 
        except Exception as e: tempstr = f"ping {ip_list[c]} failed: {e}" 
        reslist.append(tempstr) 
        print(f"{ip_list[c]}\n{reslist[c]}") 
        c += 1 

if re.match('\w+', name) != None: # type: ignore 
    if os_name == "nt": 
        if re.match(".:.+", name): # type: ignore
            fpath = name.replace(name.split('\\')[-1], '').removesuffix('\\') 
            try: f = open(f"{name}.txt", "w"); name = name.split('\\')[-1] 
            except PermissionError as pe: print(f"Please use a directory the program has permissions to write to. PermissionError: {pe}"); exit 
            except Exception as e: print(e); exit 
        else: 
            fpath = ppath[0].replace('\\\\', '\\') 
            f = open(f"{fpath}\\{name}.txt", "w") 
    else: 
        if "/" in name:
            fpath = name.replace(name.split('/')[-1], '').removesuffix('/') 
            try: f = open(f"{name}.txt", "w"); name = name.split('/')[-1] 
            except PermissionError as pe: print(f"Please use a directory the program has permissions to write to. PermissionError: {pe}"); exit 
            except Exception as e: print(e); exit 
        else: 
            fpath = ppath[0] 
            f = open(f"{fpath}/{name}.txt", "w") 

    for y in range(len(reslist)): 
        f.write(reslist[y]) 
    f.close() 

    input(f'File is available at {fpath} as {name}.txt') 
else: input('Exit program: > ') 
