'''Selection sorted algorithm'''

'''return the index of the smallest item in an arr'''
def findtheSmallest1(arr):
    smallest_item, smallest_idx = arr[0], 0

    for i in range(1, len(arr)):
        if (arr[i] < smallest_item):
            smallest_item = arr[i]
            smallest_idx = i

    return smallest_idx

'''find the smallest item and append it to a new arr, pop the smallest item at the same time'''
def selectionSorted1(arr):
    new_sorted_arr = []

    while (len(arr) != 0):
        idx = findtheSmallest1(arr)
        new_sorted_arr.append(arr.pop(idx))

    return new_sorted_arr

'''sorted an arr in-placea, O(n²)'''
def findtSmallestandSorted(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[j] < arr[i]):
                arr[i], arr[j] = arr[j], arr[i]

    return arr


arr = [7, 2, 5, 3,3, 9, 0, 11, -2, 99,0, 101]
print(findtSmallestandSorted(arr))
#print(selectionSorted2(arr))

