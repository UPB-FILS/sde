#!/bin/bash
# 10

outputfile=$1
testfile=$2


python3 busybox.py ls &> $outputfile
scriptresult=$?

node verify/ls/readDir.js `pwd` > output/ls_out

node verify/ls/ls.js output/ls_out $outputfile > $testfile 2>> $outputfile
testresult=$?

rm -f output/ls_out

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct ls does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


