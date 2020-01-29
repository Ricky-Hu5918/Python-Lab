'''for recursion practice'''

'''#1: calculate the sum of an arr'''
def sum(arr):
    if not arr:
        return 0
    else:
        return arr[0]+sum(arr[1:])

'''#2: calculate the element numbers of an arr'''
def cal_nums(arr):
    if not arr:
        return 0
    else:
        return 1 + cal_nums(arr[1:])

'''#3: find the largest element in an arr'''
def find_largestItem(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] > arr[1]:
            arr[1] = arr[0]
        return find_largestItem(arr[1:])


arr = [7, 2, 3, 4, 6]
print(find_largestItem(arr))