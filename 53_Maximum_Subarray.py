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

'''#2: 更容易理解的动态规划'''
'''
动态规划的是首先对数组进行遍历，当前最大连续子序列和为 cur_sum，结果为 max_sum
如果 cur_sum > 0，则说明 cur_sum 对结果有增益效果，则 cur_sum 保留并加上当前遍历数字
如果 cur_sum <= 0，则说明 cur_sum 对结果无增益效果，需要舍弃，则 cur_sum 直接更新为当前遍历数字
每次比较 cur_sum 和 max_sum，max_sum，遍历结束返回结果
时间复杂度：O(n)
'''
def maxSubArray3(nums):
    max_sum = nums[0]
    cur_sum = 0

    for each in nums:
        if (cur_sum > 0):
            cur_sum += each
        else:
            cur_sum = each
        print(cur_sum)
        max_sum = max(max_sum, cur_sum)

    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4] #6
# print(maxSubArray1(nums))
# print(maxSubArray2(nums))
print(maxSubArray3(nums))