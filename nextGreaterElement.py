#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 496. Next Greater Element I
"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
"""

def nextGreaterElement(nums1, nums2):
    #1 为nums2中的每个元素找到下一个大值, 并存入res表中
    res = []

    for i in range(len(nums2) - 1):
        for j in range((i+1), len(nums2)):
            if nums2[i] < nums2[j]:
                res.append(nums2[j])
                break

            if j == len(nums2) - 1:
                res.append(-1)

    res.append(-1) #最后一个元素，直接返回-1

    #2 查res表返回nums1中元素对应的大值
    reL = []
    for i in range(len(nums1)):
        reL.append(res[nums2.index(nums1[i])])
    return reL

nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums3 = [2,4]
nums4 = [1,2,3,4]
nums5 = [2,1,3,5]
nums6 = [2,0,3,1,4,5,7]
print(nextGreaterElement(nums3, nums4))