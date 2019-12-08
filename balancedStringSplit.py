#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 1221
'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
'''
'''
问题分析：分割平衡串，得到尽可能多的平衡串。这是一个适用贪心算法的问题，在适当的位置截断源串得到平衡子串，
截断后前后子串的计数不互相影响（无后效性），且所有局部最优相加即为整体的最优解。
解决思路：

设置一个'L'与'R'的差值计数器diffCount，设置一个平衡子串计数器count；
顺序遍历源串字符，遇L则diffCount+1，遇到R则diffCount-1；
每遍历一个字符检查一次diffCount是否为0，若为0则count+1
'''

def balancedStringSplit(s):
    cur, num = 0, 0
    for each in s:
        if each == "R":
            cur += 1
        else:
            cur -= 1

        if cur == 0:
            num += 1
    return num

'''    
     * 思路：来两个变量，分别记录R和L的数量，当他们相等时，sum ++,返回sum
    i,j,num = 0, 0, 0
    for each in s:
        if each == "R":
            i += 1
        else:
            j += 1
        
        if (i == j):
            num += 1
    
    return num
'''

if __name__ == '__main__':
    s = "RLRRLLRLRL"
    print(balancedStringSplit(s))