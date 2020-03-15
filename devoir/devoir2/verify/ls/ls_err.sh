#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf /bla

python3 busybox.py ls /bla/bla/bla &> $outputfile
scriptresult=$?

if [ $scriptresult != 176 ]
then
    echo "Command does not fail with exit code -80." > $testfile
    exit -1 
fi

exit 0