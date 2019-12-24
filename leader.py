'''
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of
the elements of A.
For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7)
and 5 is more than a half of 8.
Write a function
def solution(A)
that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A
occurs. The function should return −1 if array A does not have a dominator.
For example, given array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
A = [3,4,3,2,3,-1,3,3]
output = [0,2,4,6,7]
'''

'''#3: 思路就是：先找到dominator元素，再遍历输出其index'''
def leader(arr):
    rt_list = arr.copy()
    res = []

    if (len(arr) == len(set(arr))): #no repeated elements
        return -1

    while (len(set(rt_list)) != 1): #find the dominator
        for each in set(rt_list):
            rt_list.remove(each)

    if (arr.count(rt_list[0]) > (len(arr)/2)):
        for i in range(len(arr)):
            if arr[i] == rt_list[0]:
                res.append(i)
    else:
        return -1

    return res

"""#2: 常规方法，用collections库函数
import collections
def leader(arr):
    the_dominator, rt_list = 0, []
    count = collections.Counter(arr)

    for i in count:
        if (count[i] > int(len(arr)/2)):
            the_dominator = i

    if (the_dominator == 0):
        return -1
    else:
        for i in range(len(arr)):
            if (the_dominator == arr[i]):
                rt_list.append(i)

    return rt_list
"""

"""#1: 常规方法
def leader(arr):
    the_dominator, rt_list = 0, []

    for i in range(len(arr)):
        if arr.count(arr[i]) > int(len(arr)/2):
            the_dominator = arr[i]

    if (the_dominator == 0):
        return -1
    else:
        for i in range(len(arr)):
            if arr[i] == the_dominator:
                rt_list.append(i)

    return rt_list
"""

A = [3,4,3,2,3,-1,3,3]
output = [0,2,4,6,7]
B = [3,2,4,3,5,6]
C = [1,2,3,4.5]
print(leader(B))