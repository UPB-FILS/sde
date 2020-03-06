#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf /bla

python3 busybox.py mv /bla/bla/bla file &> $outputfile
scriptresult=$?

if [ $scriptresult != 1 ]
then
    echo "Command does not fail with exit code 1." > $testfile
    exit -1 
fi

exit 0