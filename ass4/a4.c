#include<stdio.h>
#include<stdlib.h>

/*
Assignment 4  specification:  Store a 2 and 3 dimensional array (with difference dimensions). 
Start from a 100x100 and go upto 10,000x10,000. 
Traverse the elements of the array row by row and column by column and time the traversal 
and compare the time differences. Run perf with the command to see which cases have lower 
cache misses
*/

#define RAND_INT_MAX 100

#ifndef DIM
#define DIM 100
#endif
#ifndef ARRAY
#define ARRAY 0
#endif

/*
	$ gcc -o a4 a4.c -ARRAY=<int> [0 for 2d | 1 for 3d] -DDIM=<dim> [-DR_TEST (to test for row order) | -DC_TEST (to test for col order)]
*/

void arr_init(int *arr, int sz) {
    for (register int i = 0; i < sz; i++)
        arr[i] = rand() % RAND_INT_MAX;
}

int main(int argc, char *argv[]) {
	/*
		argc: int conidtion to change 2d/3d array creation
				0 - create 2d array
				1 - create 3d array
	*/
	int **arr_2d;
	int ***arr_3d;

	if(ARRAY==0){
		arr_2d = (int **) malloc(sizeof(int *) * DIM);
		for (register int i = 0; i < DIM; i++) {
			arr_2d[i] = (int *) malloc(sizeof(int) * DIM);
			arr_init(arr_2d[i], DIM);
		}
	}
	else{
		arr_3d = (int ***) malloc(sizeof(int *) * DIM);
		for (register int i = 0; i < DIM; i++) {
			arr_3d[i] = (int **) malloc(sizeof(int **) * DIM);
			for (register int j = 0; j < DIM; j++) {
				arr_3d[i][j] = (int *) malloc(sizeof(int) * DIM);
				arr_init(arr_3d[i][j], DIM);
			}
		}
	}

	#ifdef RTEST
	printf("Executing row test...\n");
	for (register int i = 0; i < DIM; i++) {
		if(ARRAY==0){
			for (register int j = 0; j < DIM; j++) {
				arr_2d[i][j] = arr_2d[i][j] * 2;
			}
		}
		else{
			for (register int j = 0; j < DIM; j++){
				for (register int k = 0; k < DIM; k++) {
					arr_3d[i][j][k] = arr_3d[i][j][k] * 2;
				}
			}
		}
	}
	#endif

	#ifdef CTEST
	printf("Executing column test...\n");
	for (register int i = 0; i < DIM; i++) {
		if(ARRAY==0){
			for (register int j = 0; j < DIM; j++) {
				arr_2d[j][i] = arr_2d[j][i] * 2;
			}
		}
		else{
			for (register int j = 0; j < DIM; j++) {
				for (register int k = 0; k < DIM; k++) {
					arr_3d[i][k][j] = arr_3d[i][k][j] * 2;
				}
			}	
		}
	}
	#endif
	return 0;
}
