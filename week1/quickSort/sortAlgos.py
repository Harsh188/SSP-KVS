from operator import imod
from random import randint
from quickSort import quicksort
import cProfile

import argparse


def parseArgs():
    '''Processes arugments

    Returns: parser.parse_args(): Returns populated namespace 
    '''
    parser = argparse.ArgumentParser(description='CProfile Assignment')
    parser.add_argument("--array_index")
    return parser.parse_args()

def run_algo(n:int):
    sizes = [10000, 100000, 1000000, 10000000]
    ARRAY_LENGTH = sizes[n]
    array = [randint(0, ARRAY_LENGTH) for i in range(ARRAY_LENGTH)]
    quicksort(array)

if __name__=="__main__":
    args = parseArgs()
    n = int(args.array_index)
    run_algo(n)
