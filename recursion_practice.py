'''for recursion practice'''
'''递归recursion的前提是：找到基准条件base case和递归条件recursion case'''

'''#1: calculate the sum of an arr'''
def sum(arr):
    if not arr:  #arr==None is the base case.
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

'''#4: quick sort algorithm'''
'''steps: a选择基准值pivot，b对数组进行分区，分为比pivot大和小的两个区，c对这两个分区进行快速排序（递归）'''
def quick_sort(arr):
    if (len(arr)<2):
        return arr  #base case
    else:
        pivot = arr[0]  #recursion case
        small_items = [item for item in arr[1:] if item<pivot]
        large_items = [item for item in arr[1:] if item>=pivot]

        return (quick_sort(small_items)) + [pivot] + (quick_sort(large_items)) #ascending
        #return (quick_sort(large_items)) + [pivot] + (quick_sort(small_items)) #descending

arr = [1, 7, 2, 3, 0, 4, 6, -1, -3]
print(quick_sort(arr))
