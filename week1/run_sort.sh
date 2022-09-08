#!/usr/bin/env bash

for n in {0..4};
do
	echo $n
	python3 -m cProfile -o /home/harsh/Documents/Programming/college/SEM7/week1/profiling/bubbleSort_$n.log /home/harsh/Documents/Programming/college/SEM7/week1/profiling/sortAlgos.py --array_index=$n
done