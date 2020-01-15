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

def isPalindrome2(s):
    idx_start, idx_end = 0, len(s)-1
    while (idx_end != idx_start) or (idx_end != idx_start+1):
        if (s[idx_start] != s[idx_end]):
            return False
        else:
            idx_end -= 1
            idx_start += 1

    return True


s = "A man, a plan, a canal: Panama"
s1 = "race a car"
s2 = 'amanaplanacanalpanama'
print(isPalindrome2(s2))