'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''

'''#1: recursion version'''
def isPowerOfFour1(num):
    if (num<=0):
        return False
    elif (num == 1):
        return True
    elif (num == 2):
        return False
    else:
        return isPowerOfFour1(num/4)

'''#2: iterate version'''
def isPowerOfFour2(num):
    if (num<=0):
        return False

    while (num>=2):
        num /= 4

    return True if (num==1) else False

'''#3: enumeration version'''
def isPowerOfFour3(num):
    return True if num in list(map(lambda x:4**x, [x for x in range(20)])) else False

'''#4: xk's method'''
import math
def isPowerOfFour4(num):
    if (num<=0):
        return False

    res = (math.log10(num) / math.log10(4))
    return math.floor(res) == math.ceil(res)

'''#5: 逆推法'''
def isPowerOfFour5(num):
    if (num<=0):
        return False

    return ((4 ** round(math.log(num, 4))) == num)

num1 = 12
print(isPowerOfFour5(num1))