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

'''#2: timeout'''
from functools import reduce
def trailingZeroes2(n):
    if n==0: return n

    fac_num, res = reduce(lambda x,y:x*y,range(1,n+1)), 0

    while (fac_num > 9) and (fac_num%10 == 0):
        res += 1
        fac_num //= 10

    return res

'''#3: the amount of number 5 is the amount of number 0 in n!'''
def trailingZeroes3(n):
    res = 0
    while (n>=5):
        res += (n//5)
        n //= 5

    return res

'''#4: recursion version'''
def trailingZeroes4(n):
    if (n<5):
        return 0

    return (n//5) + trailingZeroes4(n//5)



n1 = 6109
print(trailingZeroes4(n1))