#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 35. Search Insert Position
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
"""

'''#1: nums原本是升序的，所以只需要遍历比较nums的元素与target的大小，若大于等于target说明此处就应该插入target，若全部都比target小，说明target应该插入最后 '''
def searchInsert(nums, target):
    for i in range(len(nums)):
        if (nums[i] >= target):
            return i

    return len(nums)

"""
'''#2: 直接添加target，然后排序，即使target重复，返回其下标也是OK的'''
def searchInsert(nums, target):
    nums.append(target)
    nums.sort()
    return nums.index(target)
"""

"""#3: 试着将target加入到nums中，然后返回其下标
def searchInsert(nums, target):
    if (target in nums):
        return nums.index(target)
    else:
        for i in range(len(nums)):
            if (target < nums[i]):
                nums.insert(i, target)
                break

            if (i == len(nums)-1):
                nums.append(target)

        return nums.index(target)
"""

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    target2 = 2
    target3 = 0
    target4 = 7
    print(searchInsert(nums, target4))