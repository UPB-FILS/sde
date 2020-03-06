#!/bin/bash
# 10

outputfile=$1
testfile=$2

rm -rf output/*

mkdir planet

python3 busybox.py cp planet output/express &> $outputfile
scriptresult=$?

rm -rf planet

if [ $scriptresult == 0 ]
then
    echo "cp command does not return 1 when trying to copy a directory without -r parameter." > $testfile
    exit -1
fi