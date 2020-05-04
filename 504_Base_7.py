'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''


class Solution:
    def convertToBase7_1(self, num: int) -> str:
        if num > -7 and num < 7: return str(num)

        flag, res = False, ''
        if num < 0:
            flag = True
            num = abs(num)

        while num:
            res += (str(num % 7))
            num //= 7

        if flag: res += '-'
        return res[::-1]

    def convertToBase7_2(self, num: int) -> str:
        if num > -7 and num < 7: return str(num)

        ans = []
        if num<0:
            res = '-'
            num = abs(num)
        else:
            res = ''

        while num:
            ans.append(num%7)
            num //= 7

        for i in range(len(ans)-1, -1, -1):
            res += str(ans[i])

        return res

test = Solution()
num = -79
print(test.convertToBase7_1(num), test.convertToBase7_2(num))