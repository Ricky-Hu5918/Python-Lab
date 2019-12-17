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
'''代码优化：肖哥的stack版本，没有使用下面的arr.pop(0)这种操作
    while len(input_list) > 0:
        current_char = input_list.pop(0)
'''
def removeOuterParentheses(input_str):
    input_list = list(input_str)
    left = '('
    right = ')'
    stack = []

    i = 0
    res = ''
    while (i < len(input_list)):
        current_char = input_list[i]

        if current_char == left:
            stack.append(i)    #stack仅为计数用

            if len(stack) > 1:
                res += current_char

        if current_char == right:
            stack.pop()
            if len(stack) > 0:  #stack为0，说明前面只有一个左括号，因此直接丢弃，比如S3，或者所有的右括弧都跟左括弧配对完成了
                res += current_char

        i += 1
    return res

S1 = "(()())(())" #out: ()()()
S2 = "(()())(())(()(()))" #out: ()()()()(())
S3 = "()((()))"   #out: (())
S4 = "(()(()))()" #out: ()(())
S5 = "()"
print(removeOuterParentheses(S3))
