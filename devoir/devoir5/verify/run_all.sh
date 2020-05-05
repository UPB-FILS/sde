#!/bin/bash

trap 'echo Interrupted at $(date); exit -1' INT

function run_script 
{
    name=`basename $1`
    output="output/$name"
    ref="reference/$name"

    timeout 10 node verify/verify.js $1 $> /dev/null
    if ! diff --ignore-space-change --side-by-side --suppress-common-lines $ref $output &> $output.err;
    then 
        echo "--------------" >> $errorslist 
        echo $strtitle >> $errorslist
        head -10 "$output.err" >> $errorslist
        echo >> $errorslist
        return 1
    fi
    return 0
}

DIR=`realpath $1`

POINTS=0

errorslist=$DIR/errors.out
rm -f $errorslist

cd "$DIR"

rm -rf output/*
mkdir -p output

passed=0
failed=0
total=0

for folder in verify/*
do
    if [ -d $folder ];
    then
        if [ -f "$folder"/run.txt ];
        then
            echo `head -n 1 "$folder"/run.txt`
            P=`head -n 2 "$folder"/run.txt | tail -n 1`
        else
            echo `basename $folder`
            P=10
        fi
        if [ $failed == 0 ] || ! (echo $folder | grep bonus &> /dev/null);
        then
            for script in $folder/*.js;
            do
                # title=`head -n 1 "$script" | grep '/' | cut -d "/" -f 3`
                # echo $title
                # if [ `echo -n "$title" | wc -c` -eq 0 ];
                # then
                    title=`basename $script`
                # fi
                # echo $title
                strtitle="Verifying $title"
                printf '%s' "$strtitle"
                pad=$(printf '%0.1s' "."{1..60})
                padlength=65

                if run_script $script ;
                then
                    str="ok (""$P""p)"
                    passed=$(($passed+1))
                    POINTS=$(($POINTS+$P))
                else
                    if [ $? == 124 ];
                    then
                        str="timeout (0p)"
                    else
                        str="error (0p)"
                    fi
                    failed=$(($failed+1))
                fi

                total=$(($total+1))
                printf '%*.*s' 0 $((padlength - ${#strtitle} - ${#str} )) "$pad"
                printf '%s\n' "$str"
            done
        fi
    fi
done

echo 'Tests: ' $passed '/' $total
echo 'Points: '$POINTS
echo 'Mark without penalties: '`echo $(($POINTS*100/70)) | sed 's/.$/.&/'`

if [ "$passed" != "$total" ];
then
    echo -e "Original file						      | Your file" 1>&2
    cat $errorslist 1>&2
fi