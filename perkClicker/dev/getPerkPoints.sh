#!/bin/bash
cd /home/pi/.github/phoneFarm/perkClicker/dev

#output to log file that the script is starting
current_date_time=`date "+%Y-%m-%d %H:%M:%S"`;
echo "$current_date_time - Running Script" >> /home/pi/.github/phoneFarm/perkClicker/dev/getPerkPoints.log 2>&1;
################


./pullImage.sh >> /home/pi/.github/phoneFarm/perkClicker/dev/getPerkPoints.log 2>&1
./processImage.py >> /home/pi/.github/phoneFarm/perkClicker/dev/getPerkPoints.log 2>&1




################
current_date_time=`date "+%Y-%m-%d %H:%M:%S"`;
echo "$current_date_time - Script Finished" >> /home/pi/.github/phoneFarm/perkClicker/dev/getPerkPoints.log 2>&1;
