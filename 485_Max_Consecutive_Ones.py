'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''


class Solution:
    def findMaxConsecutiveOnes2(self, nums):
        return max(len(substr) for substr in ''.join([str(x) for x in nums]).split('0'))

    '''# 1: normal way,贪心算法，每次取局部最大'''
    def findMaxConsecutiveOnes1(self, nums):
        count, max_count = 0, 0
        for each in nums:
            if each == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count

test = Solution()
nums = [0,1,1,0,1,1,1,0,0,1]
print(test.findMaxConsecutiveOnes1(nums), test.findMaxConsecutiveOnes2(nums))