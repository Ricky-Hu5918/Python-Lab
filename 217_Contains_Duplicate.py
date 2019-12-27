"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
"""

""" #1: using set() method. 136ms"""
def containsDuplicate(nums):
    return True if (len(set(nums)) < len(nums)) else False

''' #2: 140ms'''
def containsDuplicate2(nums):
    res = set()
    for each in nums:
        if each not in res:
            res.add(each)
        else:
            return True
    return False

''' #3: using Counter() method. 140ms'''
from collections import Counter
def containsDuplicate3(nums):
    #c = Counter(nums)
    #for each in list(c.values()):
    for k, v in Counter(nums).items():
        if (v > 1):
            return True
    return False

''' #3+: xk's much better version '''
from collections import Counter
def containsDuplicate33(nums):
    dict_nums = {}
    for item in nums:  #功能类似Counter，生成一个字典，key是列表元素，value是元素出现的次数
        dict_nums[item] = dict_nums.get(item, 0) + 1

    for k, v in dict_nums.items():
        if (v > 1):
            return True
    return False


''' #4: timeout'''
def containsDuplicate4(nums):
    for i in range(len(nums)):
        if (nums[i] in nums[i+1:]):
            return True

    return False

''' #5: timeout'''
def containsDuplicate5(nums):
    for item in nums:
        if nums.count(item) > 1:
            return True

    return False

''' #6: 216ms'''
def containsDuplicate6(nums):
    if (len(nums) == 1):
        return False
    else:
        nums.sort()

    for i in range(len(nums)-1):
        if (nums[i] == nums[i+1]):
            return True
    return False

nums = [1,2,3,1]
nums1 = [1]
nums2 = [1,2,3,2,2,2]
print(containsDuplicate33(nums2))