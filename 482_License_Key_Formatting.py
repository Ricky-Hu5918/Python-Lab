'''
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.
Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"
Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Example 2:
Input: S = "2-5g-3-J", K = 2
Output: "2-5G-3J"
Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.
'''

'''题目意思：除了第一组字符外，剩余的字符按照K个每组进行分组，用破折号连接起来'''
class Solution:
    def licenseKeyFormatting2(self, S: str, K: int) -> str:
        # 2: O(n)，倒序处理
        #S = S.upper()
        res = ''

        count = K
        for i in range(len(S) - 1, -1, -1):
            if S[i] != '-':
                res += S[i].upper()
                count -= 1

            if (count == 0) and (i != 0):
                count = K
                res += '-'

        return res[::-1].lstrip('-')

    # 1: normal way
    def licenseKeyFormatting1(self, S: str, K: int) -> str:
        ans = ''
        S = S.upper()   #全部变成大写字母
        for each in S:  #去掉所有破折号
            if each != '-':
                ans += each

        if len(ans)<=K: #处理长度小于K的特殊情况
            return ans

        tmp = len(ans)%K
        res = ''
        if tmp:  #处理首段字符串少于K个字符的情况
            res += ans[:tmp] + '-'

        count = 0
        for i in range(tmp, len(ans)): #剩余字符串按k个一组分组
            res += ans[i]
            count += 1

            if (count%K == 0) and (i != len(ans)-1):
                count = 0
                res += '-'

        return res

test = Solution()
S1, K1 = "--ab-3rd-0k", 3
print(test.licenseKeyFormatting1(S1, K1))
print(test.licenseKeyFormatting2(S1, K1))