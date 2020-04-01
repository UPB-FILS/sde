#!/bin/bash

trap 'echo Interrupted at $(date); exit -1' INT

function run_script 
{
    # echo $1
    name=`basename $1`
    cp $1 script.sh
    output="output/$name"

    rm -f "$output.sout"
    rm -f "$output.out"


    echo "shopt -s expand_aliases" > script_reference.sh
    echo "alias quit=exit" >> script_reference.sh
    sed 's/\(.*\)/printf \"$ \"; \1/' "script.sh" >> "script_reference.sh"

    sed 's/\(.*\)/printf \"$ \"; \1/' "script.sh" >> "output/$name.sh"

    bash script_reference.sh &> "$output.sout"
    
    if timeout 5 python3 cmd.py < script.sh &> "$output.out";
    then
        # echo "exit" >> "$output.out"
        if [ "$OUTPUTS" == "output" ];
        then
            cp "$output.sout" "$1.sout"
        fi
        sync
        if ! diff --ignore-space-change --side-by-side --suppress-common-lines "$output.sout" "$output.out" &> "$output.errors";
        then 
            echo "--------------" >> $errorslist 
            echo $strtitle >> $errorslist
            head -10 "$output.errors" >> $errorslist
            echo >> $errorslist
            return 1
        fi
    else
        RETVAL=$?
        echo "--------------" >> $errorslist 
        echo $strtitle >> $errorslist
        if [ -f "$output.err" ];
        then
            cat "$output.err" >>$errorslist
        fi
        echo >> $errorslist 
        return $RETVAL
    fi
    return 0
}

DIR=`realpath $1`

OUTPUTS=$2

POINTS=0

errorslist=$DIR/errors.out
rm -f $errorslist

cd "$DIR"

mkdir -p output
rm -rf output/*

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
            for script in $folder/*.sh;
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
echo 'Mark without penalties: '`echo $(($POINTS*100/120)) | sed 's/.$/.&/'`

if [ "$passed" != "$total" ];
then
    echo -e "Original file						      | Your file" 1>&2
    cat $errorslist 1>&2
fi