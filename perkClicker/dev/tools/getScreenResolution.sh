#!/bin/bash
deviceSerialNo=e69a57a3

#cd ~/.github/phoneFarm/perkClicker/dev/
adb -s $deviceSerialNo shell screencap -p /sdcard/screen.png
adb -s $deviceSerialNo pull /sdcard/screen.png
python getScreenResolution.py $deviceSerialNo
