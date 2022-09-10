from random import randint
import cProfile

ARRAY_LENGTH  = 10000

def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)

if __name__=="__main__":
    array = [randint(0, ARRAY_LENGTH) for i in range(ARRAY_LENGTH)]
    cProfile.run('quicksort(array)')