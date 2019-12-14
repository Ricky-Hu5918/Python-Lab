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

def singleNumber(nums):
    nums.sort()

    while (len(nums)):
        if (len(nums) == 1):
            return nums[0]

        if (nums[0] != nums[1]):
            return nums[0]
        else:
            nums.pop(0)
            nums.pop(0)

nums = [4,1,2,1,2]
print(singleNumber(nums))