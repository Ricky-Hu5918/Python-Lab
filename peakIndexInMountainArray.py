#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 852

'''
Let's call an array A a mountain if the following properties hold:
A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
'''

def peakIndexInMountainArray1(A):
    return A.index(max(A))  # 用时132ms，内存消耗13.9MB

''' #用时92ms，内存消耗13.7MB'''
def peakIndexInMountainArray2(A):
    for i in range(len(A)):  
        if ((A[i-1] < A[i]) and (A[i]>A[i+1])):
            return i 


''' #用时84ms，内存消耗13.9MB  '''
def peakIndexInMountainArray3(A):
        B = A.copy()
        print(B)
        A.sort(reverse=True)
        print(A)
        return B.index(A[0])

'''binary search, from xk'''
def peakIndexInMountainArray4(A):
    left, right = 0, len(A)-1

    while left+1<right:
        mid = (left+right)//2
        if A[mid]>A[mid+1]:
            right = mid
        else:
            left = mid

    if A[left]<A[right]:
        return right
    else:
        return left

A = [0,2,3,5,7,9,5,2,1]
print(peakIndexInMountainArray4(A))