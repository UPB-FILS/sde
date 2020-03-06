#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf output/*

python3 busybox.py cp planet express &> $outputfile
scriptresult=$?

if [ $scriptresult == 0 ]
then
    echo "cp command does not return 1 when trying to copy a non-existent file." > $testfile
    exit -1
fi