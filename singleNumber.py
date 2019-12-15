#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 136

'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1
'''

'''def singleNumber(nums):  #timeout
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]'''

#利用集合元素的去重性
def singleNumber(nums):
    return sum(set(nums)) * 2 - sum(nums)

nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6] #[4,1,2,1,2]
print(singleNumber(nums))