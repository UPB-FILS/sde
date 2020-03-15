#!/bin/bash
# 15

outputfile=$1
testfile=$2

rm -rf disney

mkdir disney
mkdir disney/mickey
touch disney/mickey/mouse
touch "disney/minnie mouse"
touch pixar

python3 busybox.py rm -R -d disney pixar &> $outputfile
scriptresult=$?

node verify/rm/rm.js disney/mickey/mouse disney/mickey "disney/minnie mouse" disney pixar> $testfile 2>> $outputfile
testresult=$?

rm -rf disney pixar

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rm does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult