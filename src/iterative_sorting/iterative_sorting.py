# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        if i != smallest_index:
            hold = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = hold

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    is_sorted = False
    while is_sorted == False:
        is_sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i+1] < arr[i]:
                hold = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = hold
                is_sorted = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # Handle edge case arr = []
    if arr == []:
        return []

    # Initialize data
    count = [0] * (max(arr) + 1)

    # Count number of elements
    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count[num] += 1

    # Modify count array so ea. index stores sum of prev. counts
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Go through arr and place them in a new array in order according to count
    places = [0] * (max(count) + 1)
    for num in arr:
        places[count[num]] = num
        count[num] -= 1

    return places[1:]