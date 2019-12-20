#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 349. Intersection of Two Arrays

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""

'''#1遍历互斥法'''
def intersection(nums1, nums2):
    res = []
    for each in nums1:
        if (each in nums2) and (each not in res):
            res.append(each)

    return res

""" #2利用集合的属性
def intersection(nums1, nums2):
    return list(set(nums1)&set(nums2))
"""

""" #3先找出所有同时存在于两个列表中的元素，然后利用集合的属性去重
def intersection(nums1, nums2):
    res = []
    for i in nums1:
        if i in nums2:
            res.append(i)
    return list(set(res))
"""

""" #4将目标容器设为集合，跟#3基本一致
def intersection(nums1, nums2):
    res = set()
    for each in nums1:
        if each in nums2:
            res.add(each)
    return list(res)
"""


nums1 = [1,2,2,1]
nums2 = [2,2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print(intersection(nums3,nums4))