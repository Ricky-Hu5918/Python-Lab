'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

'''回文串类的题目，采用双指针思路更清晰'''
class Solution:
    def validPalindrome2(self, s: str) -> bool:
        # 2: two pointers
        if (s == s[::-1]) or (s[1:] == s[1:][::-1]) or (s[:-1] == s[:-1][::-1]):
            return True

        head, tail = 0, len(s) - 1
        while head < tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
            else:
                s_head, s_tail = s[head + 1:tail + 1], s[head:tail]
                if (s_head == s_head[::-1]) or (s_tail == s_tail[::-1]):
                    return True
                else:
                    return False

        return True

    '''# 1: timeout'''
    def validPalindrome1(self, s: str) -> bool:
        if (s == s[::-1]) or (s[1:] == s[1:][::-1]) or (s[:-1] == s[:-1][::-1]):
            return True

        for i in range(1, len(s)-1):
            tmp = list(s)
            tmp.pop(i)
            if tmp == tmp[::-1]:
                return True

        return False

test = Solution()
s = "cbbcc"
print(test.validPalindrome1(s), test.validPalindrome2(s))