# RaspberryThermalPrinter
Code to setup thermal printer on Raspbian OS

first, we need to enable serial port on Raspbian OS (Raspberry pi Configuration) <br>
second, connect USB termal printer to Raspbian OS. Type ls /dev/*<br>
third, sudo chmod 666 /dev/usb/lp0 to set permission <br>
fourth, try echo -e "This is a test message.\\n\\n" > /dev/usb/lp0 to first time print <br>
fifth, install library sudo pip3 install python-escpos <br>
