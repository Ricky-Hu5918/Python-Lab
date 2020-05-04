'''
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''

class Solution:
    def findRelativeRanks(self, nums):
        tmp = nums.copy()
        tmp.sort()
        ll = len(nums)
        idx = 4
        for i in range(ll-1, -1, -1):
            if i == ll - 1:
                nums[nums.index(tmp[i])] = "Gold Medal"
            elif i == ll - 2:
                nums[nums.index(tmp[i])] = "Silver Medal"
            elif i == ll - 3:
                nums[nums.index(tmp[i])] = "Bronze Medal"
            else:
                nums[nums.index(tmp[i])] = str(idx)
                idx += 1

        return nums

test = Solution()
nums = [3, 7, 4, 2, 9]
print(test.findRelativeRanks(nums))