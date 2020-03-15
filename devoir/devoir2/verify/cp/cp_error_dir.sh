#!/bin/bash
# 10

outputfile=$1
testfile=$2

rm -rf output
mkdir output

mkdir planet

python3 busybox.py cp planet output/express &> $outputfile
scriptresult=$?

rm -rf planet

if [ $scriptresult != 166 ]
then
    echo "cp command does not return -90 when trying to copy a directory without -r parameter." > $testfile
    exit -1
fi