from random import randint
import cProfile

ARRAY_LENGTH  = 10000

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        flag = True

        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = False

        if flag:
            break

    return array

if __name__=="__main__":

    array = [randint(0, ARRAY_LENGTH) for i in range(ARRAY_LENGTH)]
    cProfile.run('bubble_sort(array)')