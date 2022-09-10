from operator import imod
from random import randint
from bubbleSort import bubble_sort
from insertionSort import insertion_sort
from mergeSort import merge_sort
from quickSort import quicksort
from countSort import countSort
# import cProfile

from pyinstrument import Profiler

def profile(size):
    # sizes = [10000, 100000, 1000000, 10000000]

    # for ARRAY_LENGTH in sizes:
    array = [randint(0, size) for i in range(1000)]
    sorted_arr = countSort(array)
    array.sort()

    if (sorted_arr == array):
        print("[INFO] Valid sort.")
    else:
        print("[ERR] Invalid sort.")

if __name__=="__main__":
    sizes = [10000, 100000, 1000000, 10000000]
    for size in sizes:
        # pr = cProfile.Profile()
        # pr.enable()

        pr = Profiler()
        pr.start()
        profile(size)
        pr.stop()
        pr.print()
        pr.output_html()
        # pr.disable() 
        # pr.dump_stats('insertion_s_' + str(size) + '.log')