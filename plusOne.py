#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 66

'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''

def plusOne(digits):
    ll = len(digits) - 1

    for i in range(ll + 1):
        if (digits[ll] == 9):
            digits[ll] = 0
            if (ll == 0):
                digits.insert(0, 1)
                break
            else:
                ll -= 1
        else:
            digits[ll] += 1
            break

    return digits


digits = [9,9,9]
print(plusOne(digits))