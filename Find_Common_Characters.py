#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 1002. Find Common Characters
"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 
Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""
def Find_Common_Characters(A):
    A_set, res = [], []

    '''先求出A0和A1的交集，这个为最大集，也是模板'''
    A1_list = list(A[1])
    for i in range(len(A[0])):
        if (A[0][i] in A1_list):
            A_set.append(A[0][i])
            A1_list.remove(A[0][i])

    '''遍历后续列表，剔除模板中不在后续列表中的元素'''
    for each in A[2:]:
        each_list = list(each)
        res = A_set.copy()
        for i in range(0, len(res)):
            if res[i] not in each_list:
                A_set.remove(res[i])
            else:
                each_list.remove(res[i])

    return A_set

A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
A1 = ["bella","label","roller"]
A2 = ["cool","lock","cook"]
print(Find_Common_Characters(A2))