'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''

'''#1: normal way, recursion'''
def addDigits1(num):
    if (num < 10):
        return num

    tmp = 0
    while (num >= 10):
        tmp += num%10
        num //= 10

    return addDigits1(tmp+num)

'''#2： same as #1'''
def addDigits2(num):
    if (num < 10):
        return num

    tmp = []
    while (num != 0):
        tmp.append(num%10)
        num //= 10

    return addDigits2(sum(tmp))

'''#3: 数位相加之后，减少的部分为9的倍数。'''
def addDigits3(num):
    if (num > 9):
        num %= 9
        if (num == 0):
            return 9

    return num

'''#4: same as #3'''
def addDigits4(num):
    if (num == 0):
        return 0
    elif (num%9 == 0):
        return 9
    else:
        return (num%9)

print(addDigits4(0)) #2
print(addDigits4(99)) #9
