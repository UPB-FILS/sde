#!/bin/bash

function run_script
{
    name=`basename $1`
    chmod u+x $1
    # in output/$name.out se va stoca outputul rularii scriptului python
    timeout 5 "./$1"  "output/$name.out" "output/$name.test" >> errors 2>&1
    result=$?
    if [ $result != 0 ]
    then
    # daca nu a facut bine, copiem ce a afisat scriptul la rulare in error.out
        echo Test $name >> "$errorslist" 2>&1
        cat "output/$name.out" >> "$errorslist" 2>> errors
        echo >> "$errorslist" 2>&1
        cat "output/$name.test" > "$hintsfile" 2>> errors
    fi
    rm -f "output/$name.test" >> errors 2>&1
    rm -f "output/$name.out" >> errors 2>&1
    return $result
}

DIR=`realpath $1`

passed=0
failed=0
total=0

POINTS=0

cd "$DIR"

errorslist=$DIR/errors.out
hintsfile=$DIR/hints.out
rm -f $errorslist
rm -f $hintsfile

for folder in verify/*
do
    if [ -d "$folder" ]
    then
        for script in $folder/*.sh
        do
            title=`basename $script`
            strtitle="Verifying $title"
            printf '%s' "$strtitle"
	        pad=$(printf '%0.1s' "."{1..60})
            padlength=65

            P=`head -n 2 "$script" | tail -n 1 | cut -d ' ' -f 2`

            if run_script $script
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
            cat "$hintsfile" 2>> errors
            rm -f "$hintsfile" 2>> errors
        done
    fi
done

echo 'Tests: ' $passed '/' $total
echo 'Points: '$POINTS
echo 'Mark without penalties: '`echo $(($POINTS/6)) | sed 's/.$/.&/'`

# afisam problemele
echo
cat $errorslist 2>> errors
echo





