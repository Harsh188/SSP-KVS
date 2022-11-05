DIM := 100

rtest2d:  a4.c
	gcc -DRTEST -DDIM=$(DIM) -ARRAY=0 -o rtest2d a4.c -O0
rtest3d:  a4.c
	gcc -DRTEST -DDIM=$(DIM) -ARRAY=1 -o rtest3d a4.c -O0
ctest2d:  a4.c
	gcc -DCTEST -DDIM=$(DIM) -ARRAY=0 -o ctest2d a4.c -O0
ctest3d:  a4.c
	gcc -DCTEST -DDIM=$(DIM) -ARRAY=1 -o ctest3d a4.c -O0

all: rtest2d ctest2d rtest3d ctest3d

clean:
	@rm -f rtest2d ctest2d rtest3d rtest3d