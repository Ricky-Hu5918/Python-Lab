#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 258
'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''

""""------3rd round------
按题目要求，不使用循环和递归！！！（参考其它人的思路）
除了传统的单纯循环，还可以找规律。假如一个三位数'abc'，其值大小为s1 = 100 * a + 10 * b + 1 * c，经过一次各位相加后，
变为s2 = a + b + c，减小的差值为(s1 -s2) = 99 * a + 9 * b，差值可以被9整除，每一个循环都这样，缩小了9的倍数。
当num小于9，即只有一位时，直接返回num，大于9时，如果能被9整除，则返回9（因为不可能返回0也不可能返回两位数及以上的值），
如果不能被整除，就返回被9除的余数。
"""

'''def addDigits(num):
    if num > 9:
        num = num % 9
        if num == 0:
            return 9
    return num
'''

def addDigits(num):
    if (num == 0):
        return 0
    elif (num%9 == 0):
        return 9
    else:
        return (num%9)


if __name__ == "__main__":
    num = 199
    print(addDigits(num))