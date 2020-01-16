"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
"""
'''#1: 常规方法，效率一般'''
def isPalindrome(s):
    if not s: return True

    list_s = list(s.lower())
    str_s = ''
    for i in range(len(list_s)):
        if (list_s[i].isalpha() or list_s[i].isnumeric()):
            str_s += list_s[i]

    return True if (str_s == str_s[::-1]) else False

'''#2: 尽可能少的使用系统自带函数'''
def isPalindrome2(s):
    if not s: return True

    str_s = ''
    for i in range(len(s)):
        if (97 <= ord(s[i]) <= 122) or (48 <= ord(s[i]) <= 57):
            str_s += s[i]
        elif (65 <= ord(s[i]) <= 90):
            str_s += chr(ord(s[i])+32)

    idx_start, idx_end = 0, len(str_s)-1
    while (idx_end != idx_start if len(str_s)%2 else idx_end > idx_start):
        if (str_s[idx_start] != str_s[idx_end]):
            return False
        else:
            idx_end -= 1
            idx_start += 1

    return True


s = "A man, a plan, a canal: Panama"
s1 = "race a car"
s2 = 'amanaplanacbanalpanama'
s3 = "a."
print(isPalindrome2(s))
