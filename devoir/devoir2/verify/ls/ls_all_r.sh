#!/bin/bash
# 25

outputfile=$1
testfile=$2

rm -rf lstest output/*

mkdir lstest 
mkdir "lstest/modern family"
mkdir "lstest/modern family/pritchett"
touch "lstest/modern family/pritchett/jay"
touch "lstest/modern family/pritchett/gloria"
touch "lstest/modern family/pritchett/joe"
mkdir "lstest/modern family/dunphy"
touch "lstest/modern family/dunphy/claire"
touch "lstest/modern family/dunphy/phil"
touch "lstest/TVshows"
touch "lstest/.hidden"
touch "lstest/modern family/dunphy/.alex"

echo "modern family" > output/ls_out
echo "TVshows" >> output/ls_out
echo "modern family/pritchett" >> output/ls_out
echo "modern family/dunphy" >> output/ls_out
echo "modern family/pritchett/jay" >> output/ls_out
echo "modern family/pritchett/gloria" >> output/ls_out
echo "modern family/pritchett/joe" >> output/ls_out
echo "modern family/dunphy/claire" >> output/ls_out
echo "modern family/dunphy/phil" >> output/ls_out
echo "." >> output/ls_out
echo ".." >> output/ls_out
echo ".hidden" >> output/ls_out
echo "modern family/." >> output/ls_out
echo "modern family/.." >> output/ls_out
echo "modern family/pritchett/." >> output/ls_out
echo "modern family/pritchett/.." >> output/ls_out
echo "modern family/dunphy/." >> output/ls_out
echo "modern family/dunphy/.." >> output/ls_out
echo "modern family/dunphy/.alex" >> output/ls_out


python3 busybox.py ls -R -a lstest &> $outputfile
scriptresult=$?

node verify/ls/ls.js output/ls_out $outputfile> $testfile 2>> $outputfile
testresult=$?

rm -rf lstest
rm -f output/ls_out

if [ $testresult == 0 ]
then
    echo "in if"
    if [ $scriptresult != 0 ]
    then
        echo "Correct ls does not return 0 exit code." > $testfile
        exit -1 
    fi
fi
exit $testresult


