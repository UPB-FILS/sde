#!/bin/bash
# 10

outputfile=$1
testfile=$2

rm -rf mickey
mkdir  mickey

python3 busybox.py rm --dir mickey &> $outputfile
scriptresult=$?

node verify/rm/rm.js mickey > $testfile 2>&2
testresult=$?

rm -df mickey

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rm does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


