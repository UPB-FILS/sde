#!/bin/bash
# 5

outputfile=$1
testfile=$2

echo "bender bending rodriguez" > lnfile

python3 busybox.py ln lnfile ln_lnfile &> $outputfile
scriptresult=$?

node verify/ln/ln.js lnfile ln_lnfile > $testfile
testresult=$?

rm -f lnfile
rm -f ln_lnfile

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct ln command does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult