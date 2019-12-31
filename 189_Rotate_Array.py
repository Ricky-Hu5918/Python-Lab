"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

'''#1: not work in leetcode env.'''
def rotate1(nums,k):
    nums = nums[-k:]+nums[:k]
    return nums

'''#2: 固定同nums[0]的值进行顺序交换，timeout'''
def rotate2(nums,k):
    while (k != 0):
        for i in range(1, len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
        k -= 1
    return nums

'''#3: 巧妙之处在于nums[(i+k)%len(nums)]，(i+k)%len(nums)取到的idx，就是右移了k位的idx'''
def rotate3(nums,k):
    tmp_nums = nums.copy()

    for i in range(len(nums)):
        nums[(i+k)%len(nums)] = tmp_nums[i]

    return nums

'''#4: 同#2，固定同nums[len(nums) - 1]的值倒序进行交换，timeout'''
def rotate4(nums,k):
    while (k != 0):
        pre = nums[len(nums) - 1]
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = pre
            pre = tmp
        k -= 1

    return nums


nums = [1,2,3,4,5,6,7]
k = 3

print(rotate4(nums,k))