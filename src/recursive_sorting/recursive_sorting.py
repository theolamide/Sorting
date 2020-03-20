# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a = 0  # Initial index of arrA
    b = 0  # Initial index of arrB

    for k in range(0, elements):
        # Check for empty array argument. If empty, defer to other array and set index k to index of other non empty array
        if a >= len(arrA):
            merged_arr[k] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1
        # Compare values arrA and arrB and set the lesser value to index k in merged_arr and iterate k
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        else:
            merged_arr[k] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        mid_arr = len(arr)//2
        left = merge_sort(arr[0:mid_arr])
        right = merge_sort(arr[mid_arr:])

        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
