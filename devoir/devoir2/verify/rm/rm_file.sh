#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf mickey

touch mickey
python3 busybox.py rm mickey &> $outputfile
scriptresult=$?

node verify/rm/rm.js mickey > $testfile 2>&2
testresult=$?

rm -f mickey

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rm does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


