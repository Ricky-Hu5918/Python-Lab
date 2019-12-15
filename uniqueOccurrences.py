#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 1207

'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
'''

def uniqueOccurrences(arr):
    cn = []
    arrSet = list(set(arr))

    for i in range(len(arrSet)):
        cn.append(arr.count(arrSet[i]))

    if (len(set(cn)) == len(cn)):
        return True
    else:
        return False


arr = [1,2,3,4,2,4]
print(uniqueOccurrences(arr))