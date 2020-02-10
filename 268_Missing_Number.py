'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

'''#1:利用元组运算，找出丢失的元素'''
def missingNumber1(nums):
    tmp = [x for x in range(len(nums))]
    k = set(tmp).difference(set(nums))
    if not k:
        return max(nums)+1
    else:
        return list(k)[0]

'''#2: 先排序，然后遍历找出前后差值不为1的元素'''
def missingNumber2(nums):
    nums.sort()
    if (nums[0] != 0):
        return 0
    for i in range(len(nums)-1):
        if (nums[i+1]-nums[i] != 1):
            return nums[i]+ 1

    return nums[-1]+1

nums1 = [9,6,4,2,3,5,7,0,1]
nums2 = [1]
nums3 = [1, 0]
print(missingNumber2(nums2))