#!/bin/bash

cd submissions_i
bash get_info.sh
bash strip_comments.sh
bash ban_imports.sh
bash final_submitter.sh
cd ..

cd submissions_f
bash run_all.sh
cd ..

cd outputs
bash compare_ans.sh
cd ..