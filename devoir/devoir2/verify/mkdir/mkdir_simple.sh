#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf out_dir

python3 busybox.py mkdir out_dir &> $outputfile
scriptresult=$?

node verify/mkdir/mkdir.js out_dir > $testfile 2>> $outputfile
testresult=$?

rm -df out_dir

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct mkdir does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult