#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf lndir
mkdir lndir

python3 busybox.py ln lndir ln_lndir &> $outputfile
scriptresult=$?

rmdir lndir

if [ $scriptresult != 1 ]
then
    echo "Command does not fail with exit code 1." > $testfile
    exit -1 
fi

exit 0