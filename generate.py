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
history 1:#思路：设定一个baseUnit列表[1,1]，将上一层列表中的元素两两相加的结果从第二个位置起开始插入baseUnit，插入次数正好等于上一层列表的长度-1，
最后将baseUnit列表append到需要返回的大列表rr，即完成了一层的列表拼接，注意完成后要将baseUnit复原。
'''
'''
history 2: #模仿肖哥的方法再写一次！！！
'''
def generate(numRows):
    if numRows<0:
        return []

    rr = [[1], [1, 1]]
    if numRows<=2:
        return rr[:numRows]

    pre_line = rr[1]

    for i in range(numRows-2):
        current_line = pre_line.copy()
        current_line.append(1)
        for j in range(len(pre_line)-1):
            current_line[j+1] = pre_line[j] + pre_line[j+1]

        rr.append(current_line)
        pre_line = current_line.copy()

    return rr

print(generate(5))