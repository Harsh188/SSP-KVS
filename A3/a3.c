#include <stdio.h>
#include <stdlib.h>

#define size 1000000

long long arr[size];

void forLoop()
{
   long long count = 0;
   for(long long i = 1; i <= size; i++)
   {
        count+=1;
   }
   printf("Finished %lld iterations!\n",count);
}

void accessArr(long long index)
{
   for(long long i = 1; i <= size; i++)
   {
        arr[i]=i;
   }
   if(index>0 && index<=size)
   {
   	printf("arr[%lld]: %lld\n",index,arr[index]);
   }
   else
   {
   	printf("Out of bound!\n");
   }
}

int main(int argc, char** argv) 
{
   /* Command line arguments for:
   	forLoop: none
   	accessArr: arr_index_from_1_to_1M
   */
   if(argv[1]==NULL)
   {
   	// Execute a for loop for a million iterations
   	forLoop();
   }
   else
   {
   	// Access a large array
   	long long index = strtoll(argv[1], NULL, 10);
   	accessArr(index);
   }
   return 0;
}
