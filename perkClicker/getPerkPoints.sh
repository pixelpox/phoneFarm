#!/bin/bash

rootDir='/home/pi/.perkClicker'
cd $rootDir

#output to log file that the script is starting
current_date_time=`date "+%Y-%m-%d %H:%M:%S"`;
echo "$current_date_time - Running Script" >> $rootDir/log/getPerkPoints.log 2>&1;
################
#test script
#./script/getPerkPoints.py

./script/getPerkPoints.py >> $rootDir/log/getPerkPoints.log 2>&1; 2>&1




################
current_date_time=`date "+%Y-%m-%d %H:%M:%S"`;
echo "$current_date_time - Script Finished" >> $rootDir/log/getPerkPoints.log 2>&1;
