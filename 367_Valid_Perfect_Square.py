'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false
'''

'''#1: 二分法'''
def isPerfectSquare1(num):
    if (num < 2):
        return True

    low, high = 2, num
    while (low < high):
        mid = (low+high)//2
        if (mid < (num/mid)):
            low = mid + 1
        else:
            high = mid

    return (low * low) == num

'''#2: 二分法'''
def isPerfectSquare2(num):
    if (num < 2):
        return True

    low, high = 2, (num//2)
    while (low <= high):
        mid = (low+high)//2
        guess_num = mid*mid
        if (guess_num == num):
            return True
        elif (guess_num < num):
            low = mid + 1
        else:
            high = mid -1

    return False

'''#3: 牛顿迭代法'''
def isPerfectSquare3(num):
    if (num < 2):
        return True

    x = (num//2)
    while (x * x > num):
        x = (x + num//x) // 2

    return x * x == num

num1 = 16
num2 = 15
print(isPerfectSquare2(num1))
print(isPerfectSquare2(num2))
print(isPerfectSquare3(num1))