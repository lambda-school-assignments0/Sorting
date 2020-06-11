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
    if len(arr) <= 1:
        return arr
    elif len(arr) % 2 == 0:
        return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))
    else:
        return merge(merge_sort(arr[:len(arr)//2+1]), merge_sort(arr[len(arr)//2+1:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    # initialize pointer to start at "2nd" array
    start2 = mid + 1

    # the two arrays should both be sorted, check if end value
    # of "first" array is less than "second" array
    # if true, then overall array should also be sorted
    if arr[mid] <= arr[start2]:
        return arr

    # traverse through arrays and compare values to see where
    # to switch values
    while start <= mid and start2 <= end:
        # if out of order
        if arr[start2] < arr[start]:
            # swap and shift everything to the right so we keep it
            # sorted
            arr[:] = arr[0:start] + [arr[start2]] + arr[start:start2] + arr[start2+1:]
            # increment pointers
            start += 1
            start2 += 1
            # (mid needs to incrememnt because we shifted to the right)
            mid += 1
        # start element is in the right place
        else:
            start += 1

    return arr


def merge_sort_in_place(arr, l, r): 
    # TO-DO
    # get middle
    if l < r:
        m = (l + r) // 2

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr