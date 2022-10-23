#!/bin/bash

for iter in {1..10}
do
    echo "Iteration $iter"
    sudo perf stat -o loops_stat_${iter}.txt -e cache-references,cache-misses,branches,branch-misses,instructions ./A3
    sudo perf stat -o shared_stat_${iter}.txt -e cache-references,cache-misses,branches,branch-misses,instructions ./A3 array
done