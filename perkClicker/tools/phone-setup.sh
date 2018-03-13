#!/bin/bash
port=5555
output=$(adb shell ifconfig wlan0)
ipAddress=$(echo $output | cut -d ' ' -f 3)
adb tcpip "$port"
echo "$ipAddress:$port"
#adb connect "$ipAddress:$port"


