#!/bin/bash
phoneSerial=e69a57a3
port=5555
output=$(adb -s $phoneSerial shell ifconfig wlan0)
ipAddress=$(echo $output | cut -d ' ' -f 3)
adb -s $phoneSerial tcpip "$port"
echo "$ipAddress:$port"
#adb -s $phoneSerial connect "$ipAddress:$port"


