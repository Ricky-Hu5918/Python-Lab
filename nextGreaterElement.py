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
'''#肖哥filter版本'''
def nextGreaterElement(nums1, nums2):
    res = []

    for each in nums1:
        idx_in_2 = nums2.index(each)

        #filtered = [x for x in nums2[idx_in_2:] if each < x]  #返回一个列表元素

        # filter(function, iterable)方法，传递一个函数和可迭代对象，返回符合函数要求的一个迭代器对象
        filtered = list(filter(lambda x: x>each, nums2[idx_in_2:] ))

        if len(filtered)>0:
            res.append(filtered[0])
        else:
            res.append(-1)

    return res


nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums3 = [2,4]
nums4 = [1,2,3,4]
nums5 = [2,1,3,5]
nums6 = [2,0,3,1,4,5,7]
print(nextGreaterElement(nums3, nums4))