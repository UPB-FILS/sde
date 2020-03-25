#!/bin/bash

if [ "$#" -lt 1 ]; 
then
	echo "Please provides the processes pid"
else
	for i in $(seq 1 100); do
		echo "sending SIGINT number $i"
		kill -SIGINT  $1
	done
fi



