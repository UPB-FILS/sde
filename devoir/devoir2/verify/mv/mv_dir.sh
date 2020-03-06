#!/bin/bash
# 5

outputfile=$1
testfile=$2

rm -rf output/*
rm -rf simpsons

mkdir simpsons
echo "ay caramba" > simpsons/bart
echo "ay caramba" > output/bart
mkdir simpsons/lisa
touch simpsons/lisa/homework
echo "150" > simpsons/lisa/mensa
echo "150" > output/lisa

python3 busybox.py mv simpsons "the simpsons" &> $outputfile
scriptresult=$?

ls simpsons &> $testfile
testresult=$?

rm -rf simpsons

if [ $testresult != 0 ]
then
    ls "the simpsons" &> $testfile
    testresult=$?
    if [ $testresult == 0 ]
    then
        (ls "the simpsons/bart" && ls "the simpsons/lisa" && ls "the simpsons/lisa/homework" && ls "the simpsons/lisa/mensa") &> $testfile
        testresult=$?
        if [ $testresult == 0 ]
        then
            (diff -q output/bart "the simpsons/bart" && diff -q output/lisa "the simpsons/lisa/mensa") > $testfile
            testresult=$?
            
            rm -rf output/* "the simpsons"
        
            if [ $testresult == 0 ]
            then
                if [ $scriptresult != 0 ]
                then
                    echo "Correct mv command does not return 0 exit code." > $testfile
                    exit -1 
                fi
            else
                echo "Destination files inside moved directory do not match initial files." > $testfile
                exit -1
            fi
        else
            rm -rf "the simpsons" output/*
            echo "Destination files inside source directory do not exist." > $testfile
            exit -1
        fi
    else
        rm -rf simpsons output/*
        echo "Destination directory does not exist." > $testfile
        exit -1
    fi
else
    rm -rf output/* "the simpsons" simpsons
    echo "Source file still exists." > $testfile
    exit -1
fi
