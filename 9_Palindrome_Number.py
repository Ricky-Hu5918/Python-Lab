"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Could you solve it without converting the integer to a string?
"""
'''#1: normal method. 76ms/12.8MB'''
def isPalindrome(x):
    if x < 0:
        return False

    res = []
    for i in range(len(str(x))):
        res.append(x%10)
        x = x//10

    if (res == res[::-1]):
        return True
    else:
        return False


x1 = 121  #true
x2 = -121 #false
x3 = 10   #false

print(isPalindrome(x3))
