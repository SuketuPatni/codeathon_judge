#!/bin/bash

TIMEFORMAT=%R

if compgen -G "*_3.py" > /dev/null; then
    for FILE in *_3.py; do
        echo --------- >> ../runtimes.txt
        echo $FILE >> ../runtimes.txt;
        length=(${#FILE}-3);
        ques_no=${FILE:1:1};
        (time cat ../inputs/input_"$ques_no".txt | python3 $FILE) 1> ../outputs/${FILE:0:$length}_out.txt 2>> ../runtimes.txt;
               

    done
fi

unset TIMEFORMAT