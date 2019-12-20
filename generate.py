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
'''
history 4: #肖哥recursion V2
'''
def pascal_triangle(n, current_row=0, prev=[]):

    # base case #1, if recursion finishes, the function should return an empty array
    if current_row > n:
        return []
    # start recursion from here, given current_row is by default 0
    elif current_row == 0:
        return pascal_triangle(n, current_row+1, [1])

    # start to do other recursion when current_row goes up, remember, variable prev will be updated after each recursion
    # it is calculated by the calculate_pascal_triangle_row function
    else:
        return [prev] + pascal_triangle(n, current_row+1, calculate_pascal_triangle_row(prev))


# let's calculate items for each recursion
def calculate_pascal_triangle_row(prev):
    res = [1] * (len(prev)+1)
    for i in range(1, len(prev)):
        res[i] = prev[i-1] + prev[i]
    return res


print(pascal_triangle(10))
