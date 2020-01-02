'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''
'''#1: 使用split方法，40ms'''
def lengthOfLastWord1(s):
    if (s.split() == []):
        return 0
    else:
        return len(s.split()[-1])


'''#2: 只处理最后一个word，24ms'''
def lengthOfLastWord2(s):
    word_start = 0
    word_end = False
    ll = len(s)-1
    while (ll >= 0):
        if (s[ll] != ' '):
            if not word_end:
                word_start += 1
            else:
                break
        else:
            if word_start:
                word_end = True
        ll -= 1

    if not word_start:
        return 0
    else:
        return word_start



s = " "
s1 = "  hello  "
s2 = "Hello World"
print(lengthOfLastWord2(s))