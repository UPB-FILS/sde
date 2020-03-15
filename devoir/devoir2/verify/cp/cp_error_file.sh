#!/bin/bash
# 5

outputfile=$1
testfile=$2

python3 busybox.py cp planet express &> $outputfile
scriptresult=$?

if [ $scriptresult != 166 ]
then
    echo "cp command does not return -90 when trying to copy a non-existent file." > $testfile
    exit -1
fi