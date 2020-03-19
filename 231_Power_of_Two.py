'''
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16
'''

'''#1: recursion version'''
def isPowerOfTwo1(n):
    if n == 0: return False
    if n == 1: return True

    if n % 2:
        return False
    else:
        return isPowerOfTwo1(n / 2)

'''#2: normal way'''
def isPowerOfTwo2(n):
    if n == 0: return False
    if n == 1: return True

    while n%2 == 0:
        n /= 2
        if n==1:
            return True

    return False

'''#3:'''
def isPowerOfTwo3(n):
    return (n > 0) and (bin(n).count('1') == 1)


n1 = 0  #false
n2 = 16 #true
n3 = 218 #false
print(isPowerOfTwo3(n2))