#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 258
""""------1st round------
#最low的版本，使用了多次重复循环。先把数字拆开，放入列表，然后计算列表中数值之和，
# 若和大于10则继续拆，连续拆三次（一般三次拆分之后数字之和必定为个位数）
"""
def addDigits(num):
    A = []
    B = []

    if (num < 10):
        return num
    else:
        while num >= 10:
            A.append(num % 10)
            num = int(num / 10)
        A.append(num)
    # print(A)

    num = 0
    for each in A:
        num += each
    if num < 10:
        return num
    else:
        while num >= 10:
            B.append(num % 10)
            num = int(num / 10)
        B.append(num)
    # print(B)

    num = 0
    for i in B:
        num += i
    if num < 10:
        return num
    else:
        A = []
        while num >= 10:
            A.append(num % 10)
            num = int(num / 10)
        A.append(num)

    num = 0
    for i in A:
        num += i

    return num

if __name__ == "__main__":
    num = 199
    print(addDigits(num))