import subprocess, os

print("This version only supports subnet masks of /24. Edit to work with more masks iuw, and submit to https://github.com/LmaosDev/lmaoscripts/tree/pingprober\n")
print(f"OS = {os.name}\n")
ip = input("Provide an ip address (wildcard = '*') > ")
name = input("Name of scan-file: > "); print("\n") 
ip_list = []; reslist = []

#for '*' in ip:
if '*' in ip:
    for i in range(255):
        ip_list.append(f'{ip.replace("*", str(i+1))}') 
else: ip_list.append(ip) 

c = 0 
print(ip_list)
for x in ip_list:
    if os.name == "posix":
        try: tempstr = subprocess.check_output(f"ping {x} -c 4", shell=True).decode()
        except Exception as e: tempstr = f"ping -c 4 {ip_list[c]} failed: {e}"
    else: 
        try: tempstr = subprocess.check_output(f"ping {x}", shell=True).decode()
        except Exception as e: tempstr = f"ping {ip_list[c]} failed: {e}" 
    reslist.append(tempstr)
    print(f"{ip_list[c]}\n{reslist[c]}")
    c += 1

f = open(f"{name}.txt", "w") 

for y in range(len(reslist)):
    f.write(reslist[y])
f.close()