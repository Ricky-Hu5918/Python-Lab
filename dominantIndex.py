#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 747

'''
In a given integer array nums, there is always exactly one largest element.
Find whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
'''

'''#2nd solution: 对原数组进行降序排列，判断第一个最大值是否大于等于次大值的两倍即可，执行时间28ms'''
def dominantIndex(nums):
    tmp = nums.copy()
    tmp.sort(reverse=True)

    if (tmp[0] >= tmp[1] * 2):
        return nums.index(tmp[0])
    else:
        return -1

''' #1st solution：对原数组进行降序排列，循环比较第一个数字是否大于等于后面所有单个数字的两倍，执行时间60ms   
    tmp = nums.copy()
    tmp.sort(reverse=True)

    for i in range(1, len(tmp)):
        if (tmp[0] >= tmp[i] * 2):
            return nums.index(tmp[0])
        else:
            return -1
'''
nums = [3, 6, 1, 0]  #[0,0,0,1]
print(dominantIndex(nums))