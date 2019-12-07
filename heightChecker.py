#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 1051
'''
输入：[1,1,4,2,1,3]
输出：3
解释：
高度为 4、3 和最后一个 1 的学生，没有站在正确的位置
'''

def heightChecker(heights):
    j = 0
    hh = sorted(heights)

    for i in range(len(heights)):
        if (hh[i] != heights[i]):
            j += 1
    print(j)
    return j

if __name__ == '__main__':
    heights = [1,1,4,2,1,3]
    heightChecker(heights)