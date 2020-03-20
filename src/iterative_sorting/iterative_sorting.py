# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    print(arr)
    if len(arr) == 0:
        return arr
    for i in range(0, len(arr)):
        get_smallest_num_and_index(i, arr)
        smallest_result = get_smallest_num_and_index(i, arr)

        # if smallest_result:
        smallest_value = smallest_result[0]
        smallest_index = smallest_result[1]

        # TO-DO: swap
        temp = arr[i]
        arr[i] = smallest_value
        arr[smallest_index] = temp

    print(arr)
    return arr


def get_smallest_num_and_index(intial_index, arr):
    smallest_num = arr[intial_index]
    smallest_index = intial_index
    for i in range(intial_index, len(arr)):
        if arr[i] < smallest_num:
            smallest_index = i
            smallest_num = arr[i]

    return(smallest_num, smallest_index)
# TO-DO:  implement the Bubble Sort function below


# selection_sort([3, 2, 4])
# selection_sort([])
# selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# selection_sort([4, 3, 8, 10, 45, 23])


def bubble_sort(arr):
    # Keep track of swap
    print(arr)
    swap = True
    while swap:
        swap = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                smaller_sorted = get_smaller([arr[i], arr[i+1]])

                smaller_value = smaller_sorted[0]
                bigger_value = smaller_sorted[1]

                arr[i] = smaller_value
                arr[i+1] = bigger_value
                swap = True

    print(arr)
    return arr


def get_smaller(arr):
    # print(arr)
    smaller_val = arr[0]
    smaller_index = 0
    if arr[1] < arr[0]:
        temp = arr[1]
        arr[1] = smaller_val
        arr[smaller_index] = temp

    # print(arr)
    return arr


# get_smaller([12, 4])

bubble_sort([15, 9, 4])


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
