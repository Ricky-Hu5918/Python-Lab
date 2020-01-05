"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

'''#1: 输入和输出都要判断是否超出范围！'''
def reverse(x):
    if (-9 <= x <= 9):
        return x

    res = []
    rt_int = 0
    res_char, res_sign = '', ''
    if x < 0:
        res_char = str(x)
        res_sign = res_char[0]
        rt_int = int(res_char[1:])
        x = rt_int

    while (x != 0):
        res.append( x %10)
        x //= 10

    ll = len(res)-1
    rt_int = 0
    for i in range(len(res)):
        rt_int += res[i]*(10**(ll-i))

    if (rt_int > (2 ** 31) - 1):
        return 0
    else:
        return int(res_sign + str(rt_int))

x0 = -3    #-3
x1 = 123   #321
x2 = -123  #-321
x3 = 120   #21
x4 = 1534236469  #0
print(reverse(x2))

