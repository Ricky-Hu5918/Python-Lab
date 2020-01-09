"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.
Return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
 
Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""
'''#1: 常规方法，使用count'''
def findSpecialInteger1(arr):
    ll = len(arr)
    for item in arr:
        if (arr.count(item)*4 > ll):
            return item

'''#2: 常规方法，使用Counter'''
from collections import Counter
def findSpecialInteger2(arr):
    for k, v in Counter(arr).items():
        if (v*4 > len(arr)):
            return k

'''#3: 常规方法，自己用字典造一个元素出现次数统计表'''
def findSpecialInteger3(arr):
    dict_arr = {}

    for item in arr:
        dict_arr[item] = dict_arr.get(item, 0) + 1

    for k, v in dict_arr.items():
        if (v*4 > len(arr)):
            return k

'''#4: 按照len/4的步长进行搜索'''
import math
def findSpecialInteger4(arr):
    ll = len(arr)
    if (ll == 1):
        return arr[0]

    search_step = 1 if (not math.ceil(ll/4)) else math.ceil(ll/4)
    idx = 0
    while (idx+search_step < ll):
        if (arr[idx] == arr[idx+search_step]):
            return arr[idx]
        else:
            idx += 1

    return arr[0]

'''#5: 思路：真正的按照len/4的步长进行搜索，因为返回值的index一定位于len/4，或者len/2，或者3*len/4的位置'''
def findSpecialInteger5(arr):
    search_step = 1 if (not len(arr)//4) else len(arr)//4

    for i in range(search_step, len(arr), search_step):
        print(arr[i], arr.count(arr[i]))
        if (arr.count(arr[i])>search_step):
            return arr[i]

    return arr[0]


arr = [1]
arr1 = [1,2,2,6,6,6,6,7,10]
arr2 = [9057,13452,13452,13452,13452,13452,14141,14448,60395,95081]
print(findSpecialInteger5(arr))