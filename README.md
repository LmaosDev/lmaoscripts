# lmaoscripts  
scripts we sometimes use  

check branches for scripts, theyre named lol  


**CATRAIN arguments:**  

* -i --ip             Target IP address (str)  
* -c --count          Packet run count (3 packets per run)  
* -s --srcip          Source IP. Default: '192.168.1.2'\nNote that if --mac == 'y'; there is no default and format is `12:90:ad:F3:7c:Eb`  
* -t --threadcount    Thread count (int)
* -f --interface      The name of the interface to use.  
                      Defaults: 'eth0' on Linux; first Ethernet interface on Windows IF --mac == 'y'. Else uses system default.  
* -p --showping       Show ping (y/n)  
* -e --hidethreads    Hide most threads from showing in UI. Recommended for 20+ threads (y/n)  
* -d --data           The data to be sent. No more than 1456 chars. Is repeated and cut off to fill up 1456 chars (default: 'HI! :3 ')  
* -r --randomsrc      Randomize the source IP. (y/n)
* -n --delay          Add a delay between packets and/or packet runs, in seconds. Format: PACKET_DELAY:RUN_DELAY
                      Use a colon ':' to specify which number is which as such;
                      \[-n PACKET_DELAY:] \[-n PACKET_DELAY] \[-n :RUN_DELAY] \[-n PACKET_DELAY:RUN_DELAY]
* -m --mac            In stead of an ip, target a mac address. \[using ip field] \(Disables pinging) (y/n)  
* --debug             Enable debug output \[show errors, stop UI resets, output settings on start] \(bool)  
* --verbose           Enable packet logs (bool)  
* --exit              Exit immediately on completion (bool)  

catrainBSOD.bat is a batch script designed to cause a BSOD on windows by calling a stupid amount of processes of catrain and itself recursively :3c  

It does not have options, youll have to edit it directly  

command_examples.bat is a batch script that shows off a few examples of using catrain, as well as all of the arguments you can pass to it ^-^  
