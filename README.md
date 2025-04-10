# lmaoscripts  
scripts we sometimes use  

check branches for scripts, theyre named lol  


**CATRAIN arguments:**  

* -i --ip             Target IP address  
* -c --count          Packet run count (3 packets per run)  
* -s --srcip          Source IP (default: 192.168.1.2)  
* -t --threadcount    Thread count  
* -p --showping       Show ping (y/n, default: y)  
* -e --hidethreads    Hide most threads from showing in UI. Recommended for 40+ threads (y/n, default: n)  
* -d --data           The data to be sent. No more than 1456 chars. Is repeated and cut off to fill up 1456 chars (default: 'HI! :3 ')
* -r --randomsrc      Randomize the source IP. (y/n, default: y)  

catrainBSOD.bat is a batch script designed to cause a BSOD on windows by calling a stupid amount of processes of catrain and itself recursively :3c  

It does not have options, youll have to edit it directly 

