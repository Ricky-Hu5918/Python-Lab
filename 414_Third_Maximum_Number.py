'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution:
    def thirdMax0(self, nums) -> int:
    # xk's method
        if (len(set(nums)) <= 2): return max(nums)

        nums = set(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))

        return max(nums)


    def thirdMax1(self, nums) -> int:
        #if (len(nums) == 1) or (len(set(nums)) == 1): return nums[0]
        if (len(set(nums)) <= 2): return max(nums)

        res, count = [], 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

            if nums[i] not in res:
                res.append(nums[i])
                count += 1

            if count == 3:
                return res[2]

        #return res[0]

    '''# 2: quicksort, not that good'''
    def thirdMax2(self, nums) -> int:
        def quicksort(nums):
            if len(nums)<2:
                return nums

            pivot = nums[0]
            low = [x for x in nums[1:] if x <= pivot]
            high = [x for x in nums[1:] if x > pivot]
            return quicksort(high) + [pivot] + quicksort(low)

        ans = quicksort(nums)
        res = []
        for each in ans:
            if each not in res:
                res.append(each)

        return res[2] if len(res)>2 else res[0]

    '''#1: set+sort'''
    def thirdMax3(self, nums) -> int:
        set_nums = list(set(nums))
        set_nums.sort(reverse=True)

        if len(set_nums) <= 2:
            return set_nums[0]

        return set_nums[2]

test = Solution()
nums = [3,3,2,2,2,2,5,5,5,7,7,7,9]
print(test.thirdMax1(nums), test.thirdMax2(nums), test.thirdMax3(nums), test.thirdMax0(nums))