"""
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
"""
'''#1: 普通方法，效率低，复杂度高'''
def isUgly1(num):
    if (num<=0):
        return False

    prime_factors = [2, 3, 5]
    count = 0

    while (num != 1):
        for each in (prime_factors):
            if not (num%each):
                num //= each
                count = 0
                break
            else:
                count += 1

        if (count >= 3):
            return False

    return True

'''#2: 拆分成了2个函数，同时使用了递归。'''
def isUgly2(num):
    if (num<=0):
        return False

    for factor in [2,3,5]: #把每个factor都除尽，最后判断num的值，为1则为True
        num = div_result(num, factor)

    return True if num == 1 else False

def div_result(num, factor):  #把一个factor除尽
    if (num%factor == 0):
        num //= factor
    else:
        return num

    return div_result(num, factor)



num = 10 #false
num1 = 80 #true
num2 = 35
print(isUgly2(num))
