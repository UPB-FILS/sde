#!/bin/bash
# 10

outputfile=$1
testfile=$2

rm -rf my_super_file
touch my_super_file

sleep 2
python3 busybox.py touch my_super_file &> $outputfile
scriptresult=$?

node verify/touch/touch.js my_super_file all > $testfile 2>> $outputfile
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
    echo "Touch on does not update access and modify times." > $testfile
    exit -1
fi

exit $testresult


