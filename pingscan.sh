#!/bin/bash

echo  "==================================================================="
echo  "|Script criado para fins didaticos - C1PH3R-UNKN0W - DESEC STUDENT|"
echo  "==================================================================="

if [ "$1" == "" ]
then
	echo "Usage mode: ./pingscan.sh 192.168.0.10 80"
else
	sudo hping3 -S -p 80 -c 1 $1 2> /dev/null | grep "flags=SA" | cut -d " " -f 2 | cut -d "=" -f 2;
fi
