'''
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0). For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

Example 1:
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

Example 2:
Input: nums = [1,1,2,3]
Output: [1,3,3]
Constraints:
2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100
'''


class Solution:
    def decompressRLElist4(self, nums):
        '''#4： 试图优化成一行代码失败'''
        print((list([nums[2 * i + 1]] * nums[2 * i] for i in range(len(nums) // 2))))

    '''# 3: 优化，list的乘法和加法,复杂度低'''
    def decompressRLElist3(self, nums):
        res = []
        for i in range(len(nums)//2):
            res += [nums[2*i+1]] * nums[2*i]

        return res

    '''# 2: 优化，但复杂度没变'''
    def decompressRLElist2(self, nums):
        res = []
        for i in range(len(nums)//2):
            res.extend([nums[2*i+1] for x in range(nums[2*i])])

        return res

    '''# 1: 暴力破解'''
    def decompressRLElist1(self, nums):
        res, idx = [], 0

        while (2 * idx + 1)<len(nums):
            for i in range(nums[2*idx]):
                res.append(nums[2*idx+1])

            idx += 1

        return res

test = Solution()
nums = [3, 15, 2, 6]
print(test.decompressRLElist1(nums), test.decompressRLElist2(nums), test.decompressRLElist3(nums))