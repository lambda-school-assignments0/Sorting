# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            arrB = arrB[1:]
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            arrA = arrA[1:]
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            arrA = arrA[1:]
        else:
            merged_arr[i] = arrB[0]
            arrB = arrB[1:]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 1:
        return arr
    elif len(arr) % 2 == 0:
        return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))
    else:
        return merge(merge_sort(arr[:len(arr)//2+1]), merge_sort(arr[len(arr)//2+1:]))

print(merge_sort([38,27,43,3,9,82,10]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
