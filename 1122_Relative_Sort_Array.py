"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""

'''#1：耗时40ms'''
def relativeSortArray(arr1, arr2):
    res = []
    for each in arr2:
        cts = arr1.count(each)
        while (cts != 0):
            res.append(each)
            arr1.remove(each)
            cts -= 1

    arr1.sort()
    return res+arr1

"""#2: 思路一样，代码更简洁一些，但是耗时52ms
def relativeSortArray(arr1, arr2):
    res = []
    for each in arr2:
        while (each in arr1):
            res.append(each)
            arr1.remove(each)

    return res+sorted(arr1)
"""
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
arr3, arr4 = [28,6,22,8,44,17], [22,28,8,6]
print(relativeSortArray(arr3,arr4))
