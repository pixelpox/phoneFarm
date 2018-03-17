#!/bin/bash
deviceSerialNo=5d74baef

rootDir='/home/pi/.perkClicker'
cd $rootDir

adb -s $deviceSerialNo shell screencap -p /sdcard/screen.png
adb -s $deviceSerialNo pull /sdcard/screen.png
python tools/getScreenResolution.py $deviceSerialNo
