# lmaoscripts  
scripts we sometimes use  

check branches for scripts, theyre named lol  


**CATRAIN arguments:**  

* -i --ip             Target IP address (str)  
* -c --count          Packet run count (3 packets per run)  
* -s --srcip          Source IP (str)  
* -t --threadcount    Thread count (int)  
* -p --showping       Show ping (y/n)  
* -e --hidethreads    Hide most threads from showing in UI. Recommended for 40+ threads (y/n)  
* -d --data           The data to be sent. No more than 1456 chars. Is repeated and cut off to fill up 1456 chars (default: 'HI! :3 ')  
* -r --randomsrc      Randomize the source IP. (y/n)  
* -m --mac            In stead of an ip, target a mac address. \[using ip field] \(Disables pinging) (y/n)  
* --debug             Enable debug output \[show errors and stop UI resets] \(bool)  
* --verbose           Enable packet logs (bool)  
* --exit              Exit immediately on completion (bool)  

catrainBSOD.bat is a batch script designed to cause a BSOD on windows by calling a stupid amount of processes of catrain and itself recursively :3c  

It does not have options, youll have to edit it directly  

command_examples.bat is a batch script that shows off a few examples of using catrain, as well as all of the arguments you can pass to it ^-^  
