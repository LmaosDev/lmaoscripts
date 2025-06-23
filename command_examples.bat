@echo off
title Example Catrain Commands :3
chcp 65001 >nul 
mode 120,50 >nul 

:start 
cls 
echo  	1) List all options uwu
echo    2a) Run and show example no. 1
echo    2b) Run and show example no. 2
echo    2c) Run and show example no. 3
echo    2d) Run and show example no. 4
echo    2e) Run and show example no. 5
echo        ^^C) exit 
set /p input= %BS% ^>  	
if /I %input% EQU 1 call :list
if /I %input% EQU 2a call :ex1
if /I %input% EQU 2b call :ex2
if /I %input% EQU 2c call :ex3
if /I %input% EQU 2d call :ex4
if /I %input% EQU 2e call :ex5
if /I %input% EQU ^C goto eof 
cls 
goto start 

:list
echo.
echo -i --ip             Target IP address (str) 
echo -c --count          Packet run count (3 packets per run) 
echo -s --srcip          Source IP (str) 
echo -t --threadcount    Thread count (int) 
echo -f --interface      The name of the interface to use.
echo                     Defaults: 'eth0' on Linux; first Ethernet interface on Windows IF --mac == 'y'. Else uses system default.
echo -p --showping       Show ping (y/n) 
echo -e --hidethreads    Hide most threads from showing in UI. Recommended for 40+ threads (y/n) 
echo -d --data           The data to be sent. No more than 1456 chars. Is repeated and cut off to fill up 1456 chars (default: 'HI! :3 ') 
echo -r --randomsrc      Randomize the source IP. (y/n) 
echo -n --delay          Add a delay between packets and/or packet runs, in seconds. Format: PACKET_DELAY:RUN_DELAY
echo                     Use a colon ':' to specify which number is which as such;
echo                     [-n PACKET_DELAY:] [-n PACKET_DELAY] [-n :RUN_DELAY] [-n PACKET_DELAY:RUN_DELAY]
echo -m --mac            In stead of an ip, target a mac address. \[using ip field] \(Disables pinging) (y/n) 
echo --debug             Enable debug output \[show errors and stop UI resets] \(bool) 
echo --verbose           Enable packet logs (bool) 
echo --exit              Exit immediately on completion (bool) 
echo.
timeout -t -1
EXIT /B

:ex1
echo python catrain.py -c 3 -t 3 -p n -i 192.168.1.1 --exit True -s 255.255.255.255 -d 'Fucky wucky~ :3'
timeout -t -1
python catrain.py -c 3 -t 3 -p n -i 192.168.1.1 --exit True -s 255.255.255.255 -d 'Fucky wucky~ :3' 
EXIT /B

:ex2
echo python catrain.py -c 3 -t 3 -p n --randomsrc n -i 8C:85:C1:7C:57:40 -m y --debug True --exit True --srcip 00:00:00:00:00:00
timeout -t -1
python catrain.py -c 3 -t 3 -p n --randomsrc n -i 8C:85:C1:7C:57:40 -m y --debug True --exit True --srcip 00:00:00:00:00:00
timeout -t -1
EXIT /B

:ex3
echo python catrain.py -c 200 -t 80 -r y -i 127.0.0.1 -e y -p y
timeout -t -1
python catrain.py -c 200 -t 80 -r y -i 127.0.0.1 -e y -p y
EXIT /B

:ex4
echo python catrain.py -i ff:ff:ff:ff:ff:ff -s ff:ff:ff:ff:ff:ff -c 10 -t 2 -f Wi-Fi -p n -e n -m y --exit True --debug True
timeout -t -1
python catrain.py -i ff:ff:ff:ff:ff:ff -s ff:ff:ff:ff:ff:ff -c 10 -t 2 -f Wi-Fi -p n -e n -m y --exit True --debug True
EXIT /B

:ex5
echo python catrain.py -i 01:23:45:67:89:ab -c 10 -t 2 -f Wi-Fi -p n -r y -e n -m y -n 10
timeout -t -1
python catrain.py -i 01:23:45:67:89:ab -c 10 -t 2 -f Wi-Fi -p n -r y -e n -m y -n 10
EXIT /B
