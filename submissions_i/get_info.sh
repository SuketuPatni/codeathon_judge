#!/bin/bash

# first file to be run on getting submissions

err_string="incorrect/invalid information formatting"

if compgen -G "*.py" > /dev/null; then
    for FILE in *.py; do
        newname=$(python3 processors/get_info.py $FILE)
        if [ "$newname" != "$err_string" ]; then
            cat $FILE >> "$newname"_2.py;
        else
            echo $err_string, $FILE moved to initial discards;
            cp $FILE ../discards_i/$FILE;
        fi
    done
fi