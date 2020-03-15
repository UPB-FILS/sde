#!/bin/bash
# 20

outputfile=$1
testfile=$2

rm -rf output
mkdir output

mkdir planet
echo "bender bending rodriguez" > planet/cpfile
mkdir planet/express
touch planet/express/leela
echo "good new everybody" > planet/express/farnsworth

python3 busybox.py cp -r planet output/express &> $outputfile
scriptresult=$?

ls output/express &> $testfile
testresult=$?

if [ $testresult == 0 ]
then
   ls output/express/cpfile && ls output/express/express && ls output/express/express/leela && ls output/express/express/farnsworth &> $testfile
    testresult=$?
    if [ $testresult == 0 ]
    then
        diff -q planet/cpfile output/express/cpfile && diff -q planet/express/farnsworth output/express/express/farnsworth
        testresult=$?
        
        rm -rf planet output/express

        if [ $testresult == 0 ]
        then
            if [ $scriptresult != 0 ]
            then
                echo "Correct ln command does not return 0 exit code." > $testfile
                exit -1 
            fi
        else
            echo "Destination files are different from source files." > $testfile
            exit -1
        fi
        rm -rf planet output/express
        exit $testresult
    else
        rm -rf planet output/express
        echo "Destination directoy contents are not correct." > $testfile
        exit -1
    fi
else
    rm -rf planet output/express
    echo "Destination directory does not exist." > $testfile
    exit -1
fi