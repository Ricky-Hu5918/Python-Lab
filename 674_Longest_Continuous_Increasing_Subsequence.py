'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
'''


class Solution:
    def findLengthOfLCIS2(self, nums):
        '''# 2: same as #1'''
        if not nums: return 0
        count, count_list = 0, []

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
            else:
                count_list.append(count)
                count = 0

        if count:
            count_list.append(count)

        return max(count_list) + 1 if count_list else 1


    '''# 1: 贪婪算法'''
    def findLengthOfLCIS1(self, nums):
        if not nums: return 0
        count, max_count = 0, 0

        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count+1 if max_count else 1

    '''# 0: better than #1'''
    def findLengthOfLCIS0(self, nums):
        if not nums: return 0
        count, max_count = 1, 1

        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count += 1
            else:
                count = 1

            if max_count<count:
                max_count = count

        return max_count

test = Solution()
nums = [1,5,3,7,48]
print(test.findLengthOfLCIS1(nums), test.findLengthOfLCIS2(nums), test.findLengthOfLCIS0(nums))