#!/bin/bash
# 10

outputfile=$1
testfile=$2

rm -rf output/*

python3 busybox.py cp -r /dev/nasty output &> $outputfile
scriptresult=$?

ls output/nasty &> $testfile
testresult=$?

if [ $testresult == 0 ]
then
    diff -q /dev/nasty output/nasty
    testresult=$?
    
    rm -f output/nasty

    if [ $testresult == 0 ]
    then
        if [ $scriptresult != 0 ]
        then
            echo "Correct cp command does not return 0 exit code." > $testfile
            exit -1 
        fi
    else
        echo "Destination file is different from output file." > $testfile
    fi
    exit $testresult

else
    rm -f output/nasty
    echo "Destination file does not exist." > $testfile
    exit -1
fi