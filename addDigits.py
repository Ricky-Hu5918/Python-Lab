#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 258
""""------2st round------
使用递归！！！
正整数拆分并相加，将相加后的新数字继续拆分和相加，直到最后相加的数字小于10，即为返回结果
"""
def addDigits(num):
    if (num < 10):
        return num

    new_num = 0
    while (num != 0):
        new_num += (num % 10)
        num = int(num / 10)

    return addDigits(new_num)

if __name__ == "__main__":
    num = 199
    print(addDigits(num))