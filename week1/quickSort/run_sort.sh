#!/usr/bin/env bash
arr_size=(10000 100000 1000000 10000000)
ind=(0 1 2 3)
for n in "${ind[@]}"
do
	echo $n
	python3 -m cProfile -o /home/pes1ug19cs455/SSP/Assignment1a/SSP-KVS/week1/quickSort_${arr_size[$n]}.log /home/pes1ug19cs455/SSP/Assignment1a/SSP-KVS/week1/sortAlgos.py --array_index=$n
done
echo "done"
