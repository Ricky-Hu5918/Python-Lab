#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 118

'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
'''
#思路：设定一个baseUnit列表[1,1]，将上一层列表中的元素两两相加的结果从第二个位置起开始插入baseUnit，插入次数正好等于上一层列表的长度-1，
最后将baseUnit列表append到需要返回的大列表rr，即完成了一层的列表拼接，注意完成后要将baseUnit复原。
'''

def generate(numRows):
    if not numRows:
        return []

    if (numRows == 1):
        return [[1]]

    if (numRows == 2):
        return [[1], [1, 1]]

    baseUnit, tmp = [1, 1], 0
    rr = [[1], [1, 1]]
    if (numRows > 2):
        for i in range(2, numRows):
            for j in range(len(rr[i - 1]) - 1):
                tmp = (rr[i - 1][j]) + (rr[i - 1][j + 1])
                baseUnit.insert(j + 1, tmp)
            rr.append(baseUnit)
            baseUnit = [1,1]

    return rr

print(generate(8))