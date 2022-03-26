#!/bin/bash

# 2nd file to be run

if compgen -G "*_2.py" > /dev/null; then
    for FILE in *_2.py; do
        length=(${#FILE}-5);
        python3 processors/remove_comments.py $FILE >> ${FILE:0:$length}_3.py;
    done
fi