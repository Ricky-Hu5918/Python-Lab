'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''

'''#1: using Counter method'''
from collections import Counter
def majorityElement1(nums):
    for k, v in Counter(nums).items():
        if v > len(nums)/2:
            return k

'''#2: same as #1, but using dictionary method'''
def majorityElement2(nums):
    dict_nums = dict()

    for each in nums:
        dict_nums[each] = dict_nums.get(each, 0) + 1

    for k, v in dict_nums.items():
        if v > len(nums)/2:
            return k

'''#3: normal method'''
def majorityElement3(nums):
    k = len(nums)//2

    for i in range(len(nums)):
        if (nums[i] == nums[i+k]):
            return nums[i]

'''#4: '''
def majorityElement4(nums):
    nums.sort()
    k = len(nums)//2

    for each in list(set(nums)):
        idx = nums.index(each)
        if (idx+k < len(nums)) and (nums[idx] == nums[idx+k]):
            return each

'''#5: '''
def majorityElement5(nums):
    nums.sort()
    return nums[len(nums)//2]

nums1 = [8,8,7,7,7]
print(majorityElement5(nums1))
