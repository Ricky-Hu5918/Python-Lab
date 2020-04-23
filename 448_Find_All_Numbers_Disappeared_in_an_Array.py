'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''


class Solution:
    def findDisappearedNumbers4(self, nums):
        return list(set(x for x in range(1, len(nums) + 1)) - set(nums))  #xk's method

    '''# 3: hashtable'''
    def findDisappearedNumbers3(self, nums):
        hastable = {}
        for each in nums:
            hastable[each] = 1

        res = []
        for num in range(1, len(nums)+1):
            if num not in hastable:
                res.append(num)

        return res

    '''# 2: 这道题巧妙之处在于(nums[i]-1)的值一定可以作为nums[i]的索引'''
    def findDisappearedNumbers2(self, nums):
        # Iterate over each of the elements in the original array
        for i in range(len(nums)):

            # Treat the value as the new index
            new_index = abs(nums[i]) - 1

            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative
            # thus indicating that the number nums[i] has
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1

        # Response array that would contain the missing numbers
        result = []

        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)

        return result


    '''# 1: my solution '''
    def findDisappearedNumbers1(self, nums):
        base_set = set(x for x in range(1, len(nums)+1))
        nums_set = set(nums)
        ans = []

        for each in base_set:
            try:
                nums_set.remove(each)
            except:
                ans.append(each)

        return ans