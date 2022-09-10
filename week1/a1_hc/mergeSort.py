from random import randint
import cProfile
ARRAY_LENGTH  = 10000

def merge(left, right):

    if len(left) == 0:
        return right
    
    if len(right) == 0:
        return left

    result = []

    index_left = index_right = 0

    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right +=1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_right == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    if len(array) < 2:
        return array

    mid  = len(array) // 2

    return merge(left = merge_sort(array[:mid]), right = merge_sort(array[mid:]))

if __name__=="__main__":
    array = [randint(0, ARRAY_LENGTH) for i in range(ARRAY_LENGTH)]
    cProfile.run('merge_sort(array)')