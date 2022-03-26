#!/bin/bash

if compgen -G "*_3.py" > /dev/null; then
    for FILE in *_3.py; do
        python3 processors/try_except.py $FILE
        mv $FILE ../submissions_f/$FILE 
    done
fi