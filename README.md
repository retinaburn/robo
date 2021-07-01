# Controlling a Robosapien V1 with an Xbox Controller

## Description

### robo.py
The python class to wrap the PiGPIO setup to generate square waves. This is all work from Carl Monk [1]

### robodriver.py
Connects to a joystick (xbox controller wired to the pi zero w) to decide what commands to send to the robo

### controller_test.py
Test program for looking at the pygame joystick codes

### robo_test.py
Test program to check sanity of communicating with the robosapien

## Thanks

[1] https://fortoffee.org.uk/2016/06/embedding-a-pizero-in-a-robosapien/


http://www.aibohack.com/robosap/ir_codes.htm




## Bluetooth Notes
sudo bash -c echo 1 > /sys/module/bluetooth/parameters/disable_ertm

sudo reboot

sudo bluetoothctl
agent on
default-agent

scan on

connect 44:16:22:AC:A9:15
trust 44:16:22:AC:A9:15

Project Scorpio: 5C:BA:37:4E:32:05
