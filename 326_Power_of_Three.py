'''
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
'''
'''#1: recursion version'''
def isPowerOfThree1(n):
    if (n==0):
        return False
    elif (n==1):
        return True
    else:
        return isPowerOfThree1(n/3)

'''#2: iterate version'''
def isPowerOfThree2(n):
    while (n>2):
        n /= 3

    return True if n==1 else False

'''#3: one-line code'''
def isPowerOfThree3(n):
    return True if n in list(map(lambda x:3**x, [x for x in range(20)])) else False

'''#4: a better version'''
def isPowerOfThree4(n):
    if (n<=0):
        return False
    else:
        return ((3**100)%n == 0)

'''#5: xk's better version'''
import math
def isPowerOfThree5(n):
    if (n<=0):
        return False

    res = (math.log10(n) / math.log10(3))
    return (math.floor(res) == math.ceil(res))


n1 = 27
n2 = 45
print(isPowerOfThree1(n1))
print(isPowerOfThree2(n1))
print(isPowerOfThree5(n2))