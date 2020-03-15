#!/bin/bash
# 15

outputfile=$1
testfile=$2

rm -rf output
mkdir output

mkdir planet
echo "bender bending rodriguez" > planet/cpfile

python3 busybox.py cp -r planet output &> $outputfile
scriptresult=$?

ls output/planet &> $testfile
testresult=$?

if [ $testresult == 0 ]
then
    ls output/planet/cpfile &> $testfile
    testresult=$?
    if [ $testresult == 0 ]
    then
        diff -q planet/cpfile output/planet/cpfile
        testresult=$?
        
        rm -rf planet output/planet

        if [ $testresult == 0 ]
        then
            if [ $scriptresult != 0 ]
            then
                echo "Correct cp command does not return 0 exit code." > $testfile
                exit -1 
            fi
        else
            echo "Destination file is different from output file." > $testfile
            exit -1
        fi
        rm -rf planet output/express
        exit $testresult
    else
        rm -rf planet output/planet
        echo "Target directoy contents are not correct." > $testfile
        exit -1
    fi
else
    rm -rf planet output/planet
    echo "Destination directory does not exist." > $testfile
    exit -1
fi