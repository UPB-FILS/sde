#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf lstest
mkdir lstest
touch lstest/test

python3 busybox.py ls lstest/test &> $outputfile
scriptresult=$?

rm -rf lstest

echo "lstest/test" > $testfile

diff -q $outputfile $testfile
if [ $? != 0 ]
then
    echo 'ls does not print file passed as parameter' > $testfile
    exit -1 
fi

exit 0


