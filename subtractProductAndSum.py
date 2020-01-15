#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 1281
'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
'''
"""思路：把整数按照个十百千等位进行拆分，取出来放入列表，最后进行produce和sum操作"""
def subtractProductAndSum(n):
    pr, su = 1, 0
    num = []
    while n >= 10:
        num.append(n % 10)
        n = int(n / 10)

    num.append(n)

    for each in num:
        pr *= each
        su += each
    return (pr - su)

'''#2: lambda'''
from functools import reduce
def subtractProductAndSum2(n):
    pr, su = 1, 0
    num = []
    while n >= 10:
        num.append(n % 10)
        n = int(n / 10)

    num.append(n)
    return (reduce(lambda x,y:x*y, num)-reduce(lambda x,y:x+y, num))

'''#3: list(str(n)), 将正整数强转成字符串再强转成列表，即可得到以每个数位组成的列表。'''
def subtractProductAndSum3(n):
    #print(list(str(n)))
    num = [int(x) for x in list(str(n))]

    return (reduce(lambda x,y:x*y, num)-reduce(lambda x,y:x+y, num))

if __name__ == '__main__':
    n = 34
    print(subtractProductAndSum3(n))