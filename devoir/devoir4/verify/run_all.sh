#!/bin/bash

trap 'echo Interrupted at $(date); exit -1' INT

REALPATH=realpath
if ! which realpath &> /dev/null;
then
    REALPATH=grealpath
fi

TIMEOUT=timeout
if ! which timeout &> /dev/null;
then
    REALPATH=gtimeout
fi

function run_script 
{
    # echo $1
    name=`basename $1`
    #cp $1 script.sh
    output="output/$name"

    rm -f "$output.$2.out"

    if $TIMEOUT 5 python3 main.py $2 3 $1 > "$output.$2.out";
    then
        #     # echo "exit" >> "$output.out"
        #if [ "$OUTPUTS" == "output" ];
        #then
        #         cp "$output.$2.out" "$1.$2.ref"
        #         echo "This file is for debugging purposes, it does not represent the output" > "$1.$2.debug"
        #         ./sde_scheduler $2 3 $1 print >> "$1.$2.debug"
        #     fi
        #     # sync
        if ! diff --ignore-space-change --side-by-side --suppress-common-lines "$1.$2.ref" "$output.$2.out" &> "$output.$2.errors";
        then 
            echo "--------------" >> $errorslist 
            echo $strtitle >> $errorslist
            head -10 "$output.$2.errors" >> $errorslist
            echo >> $errorslist
            return 1
        fi
        else
            RETVAL=$?
            echo "--------------" >> $errorslist 
            echo $strtitle >> $errorslist
            if [ -f "$output.$2.err" ];
            then
                cat "$output.$2.err" >>$errorslist
            fi
            echo >> $errorslist 
            return $RETVAL
        fi
    return 0
}

DIR=`$REALPATH $1`

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
            for script in $folder/*.pse;
            do
                title=`head -n 1 "$script" | grep '/' | cut -d "/" -f 3`
                #echo $title
                if [ `echo -n "$title" | wc -c` -eq 0 ];
                then
                    title=`basename $script`
                fi
                echo $title
                strtitle="Verifying RR $title"
                printf '%s' "$strtitle"
                pad=$(printf '%0.1s' "."{1..60})
                padlength=65

                if run_script $script "rr" ;
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

                strtitle="Verifying RRP $title"
                printf '%s' "$strtitle"
                pad=$(printf '%0.1s' "."{1..60})
                padlength=65

                if run_script $script "rrp" ;
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

                strtitle="Verifying CFS $title"
                printf '%s' "$strtitle"
                pad=$(printf '%0.1s' "."{1..60})
                padlength=65

                if run_script $script "cfs" ;
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

# for file in calculator/*.a
# do
#     head -n 1 $file | cut -d ';' -f 1
#     P=`head -n 1 $file | cut -d ';' -f 2`
#     if [ $failed == 0 ] || ! (echo $file | grep bonus &> /dev/null);
#     then
#         # STANDARDIFS=$IFS
#         IFS=$'\n'
#         for item in `tail -n +2 $file `;
#         do
#             output=`echo $item | cut -d ';' -f 1`
#             title=`echo $item | cut -d ';' -f 2`
#             input=`echo $item | cut -d ';' -f 3`
#             # echo $output
#             # inputfile=`pwd`/"$file"
#             outputfile=output/`basename "$file"`_"$output".out
#             originalfile="$file"_"$output".out
#             errorsfile=output/`basename "$file"`_"$output".err
#             # title=`head -n 1 "$file"`
#             # if [ `echo -n "$title" | wc -c` -eq 0 ];
#             # then
#             # 	title=`basename $file`
#             # fi
#             # cat $inputfile | tail -1
#             unset IFS
#             node "$1/$script" `echo $input` > homeworkoutput
#             head -8 homeworkoutput > "$outputfile"
#             tail -n +9 homeworkoutput | sed "s/ *//" | sort >> "$outputfile"
#             rm homeworkoutput
#             strtitle="Verifying $title"
#             printf '%s' "$strtitle"
#             pad=$(printf '%0.1s' "."{1..60})
#             padlength=65
#             sed "s/ALF/$AUTHOR/" "$originalfile" | sed "s/ ---/ `sed s/./-/g <<< $AUTHOR`/" | sed "s/ ___/ `sed s/./_/g <<< $AUTHOR`/" > original
#             if diff --side-by-side --suppress-common-lines --ignore-space-change original "$outputfile" &> "$errorsfile"
#             then
#                 str="ok (""$P""p)"
#                 passed=$(($passed+1))
#                 POINTS=$(($POINTS+$P))
#             else
#                 str="error (0p)"
#                 failed=$(($failed+1))
#                 echo "--------------" >> $errorslist 
#                 echo $strtitle >> $errorslist
#                 head -10 "$errorsfile" >> $errorslist
#             fi
#             rm original
#             total=$(($total+1))
#             printf '%*.*s' 0 $((padlength - ${#strtitle} - ${#str} )) "$pad"
#             printf '%s\n' "$str"
#         done
#         unset IFS 
#     else
#         echo "Not verifying bonus, you have $failed failed tests"
#     fi
# done	

echo 'Tests: ' $passed '/' $total
echo 'Points: '$POINTS
echo 'Mark without penalties: '`echo $(($POINTS)) | sed 's/.$/.&/'`

if [ "$passed" != "$total" ];
then
    echo -e "Original file						      | Your file" 1>&2
    cat $errorslist 1>&2
fi