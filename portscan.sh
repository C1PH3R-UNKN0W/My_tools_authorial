#!/bin/bash

echo "============================================================================"
echo "|Portscan feito para finalidades de estudos - C1PH3R-UNKN0W - DESEC STUDENT|"
echo "============================================================================"


if [ "$1" == "" ]
then
	echo "Usage mode: 171.16.0.19"
else
	nmap -sV -sC -vv $1

fi
