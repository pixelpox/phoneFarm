#!/bin/bash
cd ~/.github/phoneFarm/perkClicker/dev/
adb -s 709199303183 shell screencap -p /sdcard/screen.png
adb -s 709199303183 pull /sdcard/screen.png

