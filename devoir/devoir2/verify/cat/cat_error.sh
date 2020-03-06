#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf /fake

python3 busybox.py cat /fake &> $outputfile
scriptresult=$?

if [ $scriptresult == 0 ]
then
    echo "cat command does not return 1 when trying to print a non-existing file." > $testfile
    exit -1
fi