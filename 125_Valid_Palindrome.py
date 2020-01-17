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

    for i in range(len(str_s)//2):
        if (str_s[i] != str_s[len(str_s)-i-1]):
            return False

    return True
'''  #自己的处理方法，比较弱鸡，上面是肖哥的处理方法，值得学习！
    idx_start, idx_end = 0, len(str_s)-1
    while (idx_end != idx_start if len(str_s)%2 else idx_end > idx_start):
        if (str_s[idx_start] != str_s[idx_end]):
            return False
        else:
            idx_end -= 1
            idx_start += 1
'''


'''#3: xk's solution.'''
def isPalindrome3(chars):

    if len(chars) == 1 or len(chars) == 0:
        return True

    alpha_numeric_removed_chars = filter(lambda x: (ord(x) in range(65, 91)) or (ord(x) in range(48, 58)) or (ord(x) in range(97, 123)), chars)
    print(alpha_numeric_removed_chars)

    processed_chars = list(map(lambda x: chr(ord(x) - 32) if ord(x) in range(97, 123) else x, alpha_numeric_removed_chars))
    print(processed_chars)

    # print(processed_chars)
    for i in range(len(processed_chars)//2):    #值得学习！！！
        if processed_chars[i] != processed_chars[len(processed_chars)-i-1]:
            return False

    return True


s = "A man, a plan, a canal: Panama"
s1 = "race a car"
s2 = 'amanaplanacanalpanama'
s3 = "a."
print(isPalindrome2(s3))
