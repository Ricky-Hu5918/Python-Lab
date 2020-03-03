'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
'''

import string
def titleToNumber1(s):
    dict_numbers, k = dict(), 1
    for item in string.ascii_uppercase:
        dict_numbers[item] = k
        k += 1

    s_list = list(s)
    ll, tmp = len(s_list), 0
    for i in range(ll):
        tmp += dict_numbers[s_list[i]]*(26**(ll-i-1))

    return tmp

s1 = 'AB' #28
s2 = 'AAA' #703
print(titleToNumber1(s2))
