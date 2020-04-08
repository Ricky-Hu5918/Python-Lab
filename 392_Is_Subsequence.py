'''
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"
Return true.

Example 2:
s = "axc", t = "ahbgdc"
Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
'''

from collections import Counter
class Solution:
    def isSubsequence4(self, s: str, t: str) -> bool:
        i, j = 0, 0
        '''更简洁版本的双指针'''
        while (i < len(s)) and (j < len(t)):
            if (s[i] == t[j]):
                i += 1

            j += 1

        return (i == len(s))

    '''xk;s method'''
    def isSubsequence3(self, s: str, t: str) -> bool:
        for char in s:
            print(t)
            if char in t:
                t = t[t.index(char)+1:]
            else:
                return False

        return True

    '''#lj's method'''
    def isSubsequence0(self, s: str, t: str) -> bool:
        idx = -1

        for char in s:
            idx = t.find(char, idx + 1)
            if (idx == -1):
                return False

        return True

    '''双指针'''
    def isSubsequence1(self, s: str, t: str) -> bool:
        if not s: return True
        if s and not t: return False

        idx_s, idx_t = 0, 0
        while (idx_s < len(s)):
            if (s[idx_s] == t[idx_t]):
                idx_s += 1

            idx_t += 1
            if (idx_t == len(t) and (idx_s < len(s))):
                return False

        return True

    def isSubsequence2(self, s: str, t: str) -> bool:
        if not s: return True

        '''#排除掉数量不对的情况'''
        if (Counter(s) & Counter(t)) != Counter(s):
            return False

        '''# 排除掉位置不对的情况'''
        for i in range(1, len(s)):
            if (t.find(s[i], t.index(s[i-1]))) == -1:
                return False

        return True

s1, t1 = "acb", "aabdc"
s2, t2 = "axb", "adxcb"
test = Solution()
# print(test.isSubsequence1(s1,t1), test.isSubsequence1(s2, t2))
# print(test.isSubsequence2(s1, t1), test.isSubsequence2(s2, t2))
print(test.isSubsequence3(s1, t1), test.isSubsequence3(s2, t2))
a = "abcdefg"
a = a[4:] + a[3:]
print(a)