'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

class Solution:
    def twoSum4(self, numbers, target):
        # 4: two pointers, 48ms
        start, end = 0, len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]

            if numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1

    # 3: 32ms, a better solution
    def twoSum3(self, numbers, target):
        numbers_set = set(numbers)
        for each in (numbers_set):
            tmp = target - each
            if tmp in numbers_set:
                if tmp == each:
                    return [numbers.index(tmp)+1, numbers.index(tmp)+2]
                else:
                    return [min(numbers.index(each)+1, numbers.index(tmp)+1), max(numbers.index(each)+1, numbers.index(tmp)+1)]

    # 2: 2740ms
    def twoSum2(self, numbers, target):
        res = []

        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp == numbers[i]:
                return [i+1, i+2]

            if tmp in set(numbers):
                return [i+1, numbers.index(tmp) + 1]

    # 1: timeout
    def twoSum1(self, numbers, target):
        res = []

        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    res.append(i+1)
                    res.append(j+1)
                    break

        return res

test = Solution()
numbers, target = [2,7,11,15], 9
print(test.twoSum1(numbers, target))