#!/bin/bash
# 10

outputfile=$1
testfile=$2

rm -f cp_file

python3 busybox.py cp /dev/nasty cp_file &> $outputfile
scriptresult=$?

ls cp_file &> $testfile
testresult=$?

if [ $testresult == 0 ]
then
    diff -q /dev/nasty cp_file
    testresult=$?
    
    rm -f cp_file

    if [ $testresult == 0 ]
    then
        if [ $scriptresult != 0 ]
        then
            echo "Correct ln command does not return 0 exit code." > $testfile
            exit -1 
        fi
    else
        echo "Destination file is different from output file." > $testfile
    fi
    exit $testresult

else
    rm -f cp_file
    echo "Destination file does not exist." > $testfile
    exit -1
fi
