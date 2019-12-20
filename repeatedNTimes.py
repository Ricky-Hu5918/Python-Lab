#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 961
"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
"""

'''
#1: pop方法，先从原列表中弹出一个element，然后再检查这个element是否还在列表中，在的话就是那个重复的数字。
'''
def repeatedNTimes(A):
    for i in range(len(A)):
        res = A.pop()
        if res in A:
            return res

"""
#2：利用数组切片的方式，遍历第i个元素是否在以i+1开始的切片列表中
def repeatedNTimes(A):
    for i in range(len(A)):
        if (A[i] in A[(i+1):]):
            return A[i]
"""

"""
#3：利用set属性
def repeatedNTimes(A):
    res = set()
    for each in A:
        if each in res:
            return each
        else:
            res.add(each)
"""

'''
:4：用sort方法的版本
def repeatedNTimes(A):
    A.sort()
    for i in range(len(A)):
        if (A[i] == A[i+1]):
            return A[i]
'''

'''    
#5：recursion version
def repeatedNTimes(A):
    try:
        return A.pop(A.index(A[0], 1, len(A)))
    except ValueError:
        A.pop(0)

    return repeatedNTimes(A)
'''

A1 = [1,2,3,3]
A2 = [2,1,2,5,3,2]
A3 = [5,1,5,2,5,3,5,4]
print(repeatedNTimes(A3))