#!/bin/bash

if  [ $# -eq 0 ]; then
	rbeam=25
	f1=10
	f2=20
else
	rbeam=$1
	f1=$2
	f2=$3
fi

param=($rbeam $f1 $f2)

python3 BeamMag.py "${param[@]}"


