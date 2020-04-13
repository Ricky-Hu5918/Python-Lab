'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
from collections import Counter
def longestPalindrome(s):
    count, flag = 0, 0

    for v in Counter(s).values():
        if v%2 == 0:
            count += v
        else:
            flag = 1
            count += (v-1)

    return count+flag

'''xk's better solution'''
def longestPalindrome2(s):
    res = 0

    for each in set(s):
        res += (s.count(each)//2)*2

    if res <len(s):
        return res+1
    else:
        return res


s1 = "bccccddeetyu"  #7
print(longestPalindrome(s1))
print(longestPalindrome2(s1))