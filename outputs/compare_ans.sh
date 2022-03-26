#!/bin/bash

if compgen -G "*_3_out.txt" > /dev/null; then
    for FILE in *_3_out.txt; do
        ques_no=${FILE:1:1}
        echo --------- >> ../stati.txt;
        echo $FILE >> ../stati.txt;
        python3 compare_ans.py $FILE >> ../stati.txt;
    done
fi