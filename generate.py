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
'''
history 3: #肖哥recursion方式
'''
def pascal_triangle_line(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        new_row = [1]
        last_row = pascal_triangle_line(n-1)
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
    return new_row

def pascal_triangle(n):
    res = []
    for i in range(1, n+1):
        res.append(pascal_triangle_line(i))
    return res

print(pascal_triangle(3))
