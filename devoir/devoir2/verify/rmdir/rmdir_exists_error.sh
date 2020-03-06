#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf futurama

python3 busybox.py rmdir futurama &> $outputfile
scriptresult=$?

if [ $scriptresult != 1 ]
then
    echo "Command does not fail with exit code 1 when trying to delete a folder that does not exist." > $testfile
    exit -1 
fi

exit 0


