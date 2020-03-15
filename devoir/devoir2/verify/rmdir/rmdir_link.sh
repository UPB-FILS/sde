#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf output/*
mkdir output/fry

python3 busybox.py rmdir output/fry &> $outputfile
scriptresult=$?

node verify/rmdir/rmdir.js output/fry > $testfile 2>> $outputfile
testresult=$?

rm -df output/fry

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rmdir command does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


