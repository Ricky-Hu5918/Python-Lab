#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 1021
"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
"""
'''代码优化：用一个变量j来标记'''
def removeOuterParentheses(S):
    res = ''
    m, j = 0, 0
    for i in range(len(S)):
        if S[i]=='(':
            j += 1
        elif S[i]==')':
            j -= 1

        if (j == 0):
            res += S[(m + 1):i]
            m = i+ 1

    return res

S1 = "(()())(())" #out: ()()()
S2 = "(()())(())(()(()))" #out: ()()()()(())
S3 = "()((()))"   #out: (())
S4 = "(()(()))()" #out: ()(())
S5 = "()"
print(removeOuterParentheses(S5))
