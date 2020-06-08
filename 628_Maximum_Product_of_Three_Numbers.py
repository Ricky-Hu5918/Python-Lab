'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''

'''排序之后最大乘积就两种情况：1、如果全是正数就是最后三个数相乘 2、如果有负数,最大的乘积要么是最后三个数相乘，要么是两个最小的负数相乘再乘以最大的正数'''
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
    #3: better than #2
        nums.sort()
        return max(nums[-1]*nums[0]*nums[1], nums[-1]*nums[-2]*nums[-3])

    #2: better than #1
        # nums.sort()
        # if (nums[-1]>0) and (nums[1]<0):
        #     return max(nums[-1]*nums[0]*nums[1], nums[-1]*nums[-2]*nums[-3])
        # else:
        #     return nums[-1]*nums[-2]*nums[-3]

    #1: original （枚举所有情况）
        # if len(nums)==3:
        #     return nums[0]*nums[1]*nums[2]

        # nums.sort()
        # if (nums[-1]<=0) or (nums[0]>=0):
        #     return nums[-1]*nums[-2]*nums[-3]
        # elif (nums[-1]>0) and (nums[1]<0):
        #     return max(nums[-1]*nums[0]*nums[1], nums[-1]*nums[-2]*nums[-3])
        # else:
        #     return nums[-1]*nums[-2]*nums[-3]
