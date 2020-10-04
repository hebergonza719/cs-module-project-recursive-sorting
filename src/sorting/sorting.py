# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    k = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arrB[j]
            k += 1
            j += 1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # this is where it stops
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

# a = [11, 22, 33, 44, 55, 66, 77]
# b = [13, 25, 32, 46, 52, 67, 71]
c = [22, 44, 66, 23, 42, 73, 24, 99]

# print(merge(a, b))

print(merge_sort(c))