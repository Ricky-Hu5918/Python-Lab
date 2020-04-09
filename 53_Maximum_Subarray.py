'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

'''#1: 贪心算法'''
def maxSubArray1(nums):
    cur_sum, max_sum = nums[0], nums[0]

    for each in nums[1:]:
        cur_sum = max(each, cur_sum + each)
        max_sum = max(cur_sum, max_sum)

    return max_sum

'''#2: 动态规划'''
def maxSubArray2(nums):
    max_sum = nums[0]

    for i in range(1, len(nums)):
        if (nums[i-1] > 0):
            nums[i] += nums[i-1]

        max_sum = max(nums[i], max_sum)

    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4] #6
print(maxSubArray1(nums))
print(maxSubArray2(nums))
