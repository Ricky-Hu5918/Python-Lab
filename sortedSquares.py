#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 977
"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, 
also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""
'''以下两种方式均借助了排序方法，耗时在250ms左右'''
''' #1
def sortedSquares(A):
    for i in range(len(A)):
        A[i] *= A[i]
    A.sort()
    return A
'''

''' #2
def sortedSquares(A):
    return sorted([i**2 for i in A])
'''

''' #3: 用了冒泡排序，但timeout了
def sortedSquares(A):
    for i in range(len(A)):
        A[i] *= A[i]

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i]>A[j]):
                A[i], A[j] = A[j], A[i]

    return A
'''

'''用了所谓的双指针，首尾比较，将最大的放在最前面，最后再排序'''
def sortedSquares(A):
    i, j = 0, len(A)-1
    res = []

    while (i <= j):
        if (A[i]*A[i]>A[j]*A[j]):
            res.append(A[i]*A[i])
            i += 1
        else:
            res.append(A[j]*A[j])
            j -= 1

    return res[::-1]


l1 = [-5,-2,1,3,6]
print(sortedSquares(l1))