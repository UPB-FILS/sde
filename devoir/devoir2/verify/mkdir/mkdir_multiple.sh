#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf harry potter dumbledore

python3 busybox.py mkdir harry potter dumbledore &> $outputfile
scriptresult=$?

node verify/mkdir/mkdir.js harry potter dumbledore > $testfile
testresult=$?

rm -df harry potter dumbledore

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct mkdir does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


