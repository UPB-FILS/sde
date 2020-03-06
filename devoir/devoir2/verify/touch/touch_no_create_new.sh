#!/bin/bash
# 10

outputfile=$1
testfile=$2

rm -rf my_super_file

python3 busybox.py touch -c my_super_file &> $outputfile
scriptresult=$?

ls my_super_file &> $testfile
testresult=$?

rm -rf my_super_file

if [ $testresult != 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct touch command does not return 0 exit code." > $testfile
        exit -1 
    fi
else
    echo "Touch -c creates new file." > $testfile
    exit -1
fi

exit $testresult


