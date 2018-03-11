#!/bin/bash
cd /home/pi/.github/phoneFarm/perkClicker/dev
numberOfDevices=$(cat devices.json | jq -r '.devices | length')
echo $numberOfDevices


#output to log file that the script is starting
current_date_time=`date "+%Y-%m-%d %H:%M:%S"`;
echo "$current_date_time - Running Script" >> /home/pi/.github/phoneFarm/perkClicker/dev/getPerkPoints.log 2>&1;
################

#
for i in $(seq 0 $(($numberOfDevices-1)));
do
	echo "$i - hello"
	command="cat devices.json | jq -r '.devices' "
	commandoutput=$($command)
	echo $commandoutput
	#script="cat devices.json | jq -r '.devices | .[$i] | .serialNumber'"
	#sn=eval $script
	#echo $sn

#$(cat devices.json | jq -r '.devices | .['"$i"'] | .serialNumber')
#	serialNumber=$(cat devices.json | jq -r '.devices | .[$i] | .serialNumber)
#	resolution=$(cat devices.json | jq -r '.devices | .[$i] | .resolution')
#	pin=$(cat devices.json | jq -r '.devices | .[$i] | .pin')
done
exit 1
./pullImage.sh >> /home/pi/.github/phoneFarm/perkClicker/dev/getPerkPoints.log 2>&1
./processImage.py >> /home/pi/.github/phoneFarm/perkClicker/dev/getPerkPoints.log 2>&1




################
current_date_time=`date "+%Y-%m-%d %H:%M:%S"`;
echo "$current_date_time - Script Finished" >> /home/pi/.github/phoneFarm/perkClicker/dev/getPerkPoints.log 2>&1;
