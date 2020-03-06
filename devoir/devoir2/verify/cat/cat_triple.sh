#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf output/*

echo "donuts" > output/homer
echo "ay caramba" > output/bart
echo "donuts" > output/cat_reference
echo "ay caramba" >> output/cat_reference
cat /dev/nasty >> output/cat_reference

python3 busybox.py cat output/homer output/bart /dev/nasty &> $outputfile
scriptresult=$?

if [ $scriptresult == 0 ]
then
    diff -q output/cat_reference $outputfile &> $testfile
    testresult=$?

    rm -rf output/*

    if [ $testresult != 0 ]
    then
        echo "Incorrect output."
        exit -1
    fi
else
    rm -rf output/*
    echo "Command does not return 0." > $testfile
    exit -1
fi