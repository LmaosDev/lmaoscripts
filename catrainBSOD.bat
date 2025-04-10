@echo off

for %%i in (69) do (
    start cmd /S /K "python catrain.py -i 127.0.0.1 -p n -e y -s 127.0.0.1 -d 'GetPrankd ' -c 696969 -t 24" 
    start catrainBSOD.bat 
) 
