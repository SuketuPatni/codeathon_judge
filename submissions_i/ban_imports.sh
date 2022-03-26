#!/bin/bash

if compgen -G "*_3.py" > /dev/null; then
    for FILE in *_3.py; do
        if [[ $(cat $FILE) == *"import"* ]]; then
            echo "$FILE used imports, file moved to initial discards"
            mv $FILE ../discards_i/$FILE
        fi
    done
fi