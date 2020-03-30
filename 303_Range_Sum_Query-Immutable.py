'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''

'''#1: timeout'''
class NumArray1:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        self.result = 0
        for i in range(i, ( j +1)):
            self.result += self.nums[i]

        return self.result

'''#2: recursion version, timeout'''
class NumArray2:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        if (i == j):
            return self.nums[i]

        return (self.nums[i] + self.sumRange(i+1, j))

'''#3: using built-in method, no timeout but not that good'''
class NumArray3:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:(j+1)])

'''#4: 重新构造一个列表，存储截止到当前位置的nums中所有元素之和'''
class NumArray4:
    def __init__(self, nums):
        if nums:
            self.sums = [-1 for x in range(len(nums))]
            self.sums[0] = nums[0]

            for i in range(1, len(nums)):
                self.sums[i] = self.sums[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if (i == 0):
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]


'''#5: xk's better solution, 更简洁'''
class NumArray5:
    def __init__(self, nums):
        self.sums = []
        subsum = 0

        for i in range(0, len(nums)):
            subsum += nums[i]
            self.sums.append(subsum)

    def sumRange(self, i: int, j: int) -> int:
        if (i == 0):
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]

nums = [-2, 0, 3, -5, 2, -1]
na = NumArray5(nums)
print(na.sumRange(0,2))  #1
print(na.sumRange(2,5))   #-1
print(na.sumRange(0,5))   #-3