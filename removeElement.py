#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 27. Remove Element
"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
"""

'''#4：返回长度值x，且列表中前x个数必须为原来不是val的元素'''
def removeElement(nums, val):
    not_repeated_list = []
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            not_repeated_list.append(nums[i])
            count += 1

    #去掉下面这个for循环的话，虽然不影响count的值，但是nums列表没有任何变化
    for j in range(count):
        nums[j] = not_repeated_list[j] #用非val的元素去覆盖原列表中前count个元素

    return count


"""
'''#3: 为什么这种解法在pycharm中可以正确返回，但是在leetcode中却不行呢？'''
'''答复：题目除了要求返回正确的长度外，还需要原列表前面的元素为非val的元素'''
def removeElement(nums, val):
    res = len(nums)

    for each in nums:
        if (each == val):
            res -= 1

    return res
"""

"""#2
def removeElement(nums, val):
    while val in nums:
        nums.remove(val)

    return len(nums)
"""

""" #1
def removeElement(nums, val):
    while nums.count(val):
        nums.remove(val)

    return len(nums)
"""

nums = [0,1,2,2,3,0,4,2,5,5,5]
val = 5
print(removeElement(nums,val))