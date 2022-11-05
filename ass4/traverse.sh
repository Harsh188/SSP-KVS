#!/bin/bash

dim=(100 500 1000 1500)

for d in ${dim[@]};
do
	echo $d
	(make all DIM=$d) 
	(sudo taskset -c 0 perf stat -e cache-misses ./ctest2d) &> ctest_2d_$d.txt
	(sudo taskset -c 0 perf stat -e cache-misses ./ctest3d) &> ctest_3d_$d.txt
	(sudo taskset -c 0 perf stat -e cache-misses ./rtest2d) &> rtest_2d_$d.txt
	(sudo taskset -c 0 perf stat -e cache-misses ./rtest3d) &> rtest_3d_$d.txt
	(make clean)
done
