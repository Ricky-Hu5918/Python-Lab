'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''

import math
class Solution:
    def arrangeCoins2(self, n: int) -> int:
        # 2：binary research
        start, end = int(math.sqrt(n)), n // 2 + 2
        mid = (end+start)//2

        while start <= end:
            #mid = (end + start) // 2  #这行代码放这里就不行
            #print(mid, start, end)
            if (mid * (mid + 1) // 2) > n:
                end = mid - 1
                mid = (end+start)//2
            elif (mid * (mid + 1) // 2) < n:
                start = mid + 1
                mid = (end+start)//2
            else:
                return mid

        return mid

    '''    # 1： 暴力破解法'''
    def arrangeCoins1(self, n: int) -> int:
        if n<2: return n

        sum_n = 0
        for i in range(1, n+1):
            sum_n += i
            if sum_n>n:
                break

        return i-1

n = 7
test = Solution()
print(test.arrangeCoins1(n), test.arrangeCoins2(n))