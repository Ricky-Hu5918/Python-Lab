'''
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537

Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
'''

'''The tribonacci series is a generalization of the Fibonacci sequence 
where each term is the sum of the three preceding terms.'''

class Solution:
    def tribonacci2(self, n: int) -> int:
    # 2: recursion method, timeout in leetcode
        if n == 0: return 0
        if n <= 2: return 1

        return self.tribonacci2(n - 3) + self.tribonacci2(n - 2) + self.tribonacci2(n - 1)

    '''# 1: iteration method'''
    def tribonacci1(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1

        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        for i in range(3, n+1):
            t0, t1, t2 = t1, t2, t0+t1+t2

        return t2

test = Solution()
print(test.tribonacci1(25), test.tribonacci2(25))