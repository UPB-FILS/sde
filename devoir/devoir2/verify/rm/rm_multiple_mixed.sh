#!/bin/bash
# 15

outputfile=$1
testfile=$2


touch mickey
mkdir pluto

python3 busybox.py rm --R mickey pluto &> $outputfile
scriptresult=$?

node verify/rm/rm.js mickey pluto > $testfile 2>&2
testresult=$?

rm -rf mickey pluto

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rm does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


