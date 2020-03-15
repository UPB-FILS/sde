#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf mickey

python3 busybox.py rm mickey &> $outputfile
scriptresult=$?


if [ $scriptresult != 186 ]
then
    echo "Command does not fail with exit code -70 when trying to remove a non-existing file/directory." > $testfile
    exit -1 
fi

exit 0


