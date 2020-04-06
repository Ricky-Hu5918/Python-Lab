'''
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''

'''#1: binary research'''
def mySqrt1(x):
    if (x == 0): return 0

    low, high = 1, x//2
    while (low < high):
        mid = (low + high + 1) >> 1 #取右中位数
        if (mid * mid > x):
            high = mid - 1
        else:
            low = mid

    return low

'''#2: binary research'''
def mySqrt2(x):
    if (x < 2):
        return x

    low, high = 2, x
    while (low <= high):
        mid = (low + (high-low)//2)
        if (mid > x//mid):
            high = mid - 1
        elif (mid == (x//mid)):
            return mid
        else:
            low = mid + 1

    '''返回low的话，需要判断一下，也可直接返回high'''
    # return low if (low * low <= x) else low-1
    return high

'''#3: 牛顿迭代法'''
def mySqrt3(x):
    if (x < 2):
        return x

    num = (x//2)
    while (num * num > x):
        num = (num + (x//num)) // 2

    return num


x1, x2, x3 = 6, 15, 16
print(mySqrt1(x1), mySqrt1(x2), mySqrt1(x3))
print(mySqrt2(x1), mySqrt2(x2), mySqrt2(x3))
print(mySqrt3(x1), mySqrt3(x2), mySqrt3(x3))