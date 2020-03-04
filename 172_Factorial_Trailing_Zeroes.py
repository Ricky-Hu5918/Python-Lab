'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''

'''#1: timeout'''
def trailingZeroes1(n):
    def factorialNum(n):
        if n <= 1:
            return n
        return n*(factorialNum(n-1))

    fac_num = factorialNum(n)
    res = 0
    while (fac_num > 9) and (fac_num%10 == 0):
        res += 1
        fac_num //= 10

    return res

'''#2: '''
def trailingZeroes2(n):
    fac_num, res = 1, 0

    while (n>1):
        fac_num *= n
        n -= 1

    while (fac_num > 9) and (fac_num%10 == 0):
        res += 1
        fac_num //= 10

    return res

n1 = 6109
print(trailingZeroes2(n1))