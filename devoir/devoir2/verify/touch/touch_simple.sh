#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf my_super_file
python3 busybox.py touch my_super_file &> $outputfile
scriptresult=$?

ls my_super_file &> $testfile
testresult=$?

rm -rf my_super_file

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct touch command does not return 0 exit code." > $testfile
        exit -1 
    fi
else
    echo "Touch on new file does not create it." > $testfile
    exit -1
fi

exit $testresult


