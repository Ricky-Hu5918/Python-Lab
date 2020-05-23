'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
'''

class Solution:
    def canPlaceFlowers2(self, flowerbed, n):
        # 2: 首尾分别加上0，还是以是否为连续三个0作为判断条件
        count = 0
        tmp = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) + 1):
            if (tmp[i-1] == 0) and (tmp[i] == 0) and (tmp[i+1] == 0):
                tmp[i] = 1
                count += 1

        return count >= n

    '''# 1: 针对三种情况分别进行判定是否存在连续的三个0，分别是0在首位，0在中间，和0在末尾'''
    def canPlaceFlowers1(self, flowerbed, n):
        idx, count = 0, 0
        while idx < len(flowerbed):
            if (flowerbed[idx] == 0) and ((idx==len(flowerbed)-1) or (flowerbed[idx+1] == 0)) \
                and (idx==0 or (flowerbed[idx-1] == 0)):
                flowerbed[idx] = 1
                count += 1
            idx += 1

        return count>=n

test = Solution()
flowerbed, n = [0,0,1,0,0,1], 2
print(test.canPlaceFlowers1(flowerbed, n), test.canPlaceFlowers2(flowerbed, n))