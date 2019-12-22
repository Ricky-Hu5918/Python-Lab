#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 704. Binary Search
"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

def search_binary(nums, target):
    start_idx, end_idx = 0, (len(nums)-1)
    if (start_idx == end_idx): # nums has only 1 element.
        if (target == nums[start_idx]):
            return start_idx
        else:
            return -1

    while (start_idx <= end_idx):
        mid = int(start_idx + (end_idx-start_idx)/2)

        if (target == nums[mid]):
            return mid

        if (target > nums[mid]):
            start_idx = mid + 1
        else:
            end_idx = mid - 1

    return -1


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    target2 = 2
    target3 = -5
    nums1 = [2, 5]
    nums2 = [5]
    print(search_binary(nums2, target3))