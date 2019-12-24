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
'''#二分法的版本，注意while循环的判断条件，有时需要>=,有时只需要>'''
def searchInsert(nums, target):
    start_idx, end_idx = 0, len(nums) - 1

    while start_idx < end_idx:
        mid = int(start_idx + (end_idx - start_idx) / 2)

        if (target == nums[mid]):
            return mid

        if (target > nums[mid]):
            start_idx = mid + 1
        else:
            end_idx = mid - 1

    #print(start_idx, end_idx)
    return start_idx+1 if target > nums[start_idx] else start_idx

"""
'''#1: nums原本是升序的，所以只需要遍历比较nums的元素与target的大小，若大于等于target说明此处就应该插入target，若全部都比target小，说明target应该插入最后 '''
def searchInsert(nums, target):
    for i in range(len(nums)):
        if (nums[i] >= target):
            return i

    return len(nums)
"""

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
    nums1 = [2,5]
    nums2 = [2]
    print(searchInsert(nums1, target3))