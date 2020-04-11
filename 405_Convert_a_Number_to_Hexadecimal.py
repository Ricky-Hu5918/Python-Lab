'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
'''


class Solution:
    def toHex1(self, num: int) -> str:
        # 3:
        return hex(num & 0xffffffff)[2:]

    def toHex2(self, num: int) -> str:
        #2:
        if num == 0: return "0"
        ans, rlt = [], ''

        if num < 0:
            num += 0xffffffff + 1

        while (num != 0):
            ans.append(num%16)
            num //= 16

        for i in range(len(ans)-1, -1, -1):
            if ans[i]>=10:
                rlt += chr(87+ans[i])  #a=97
            else:
                rlt += str(ans[i])

        return (rlt)

    def toHex3(self, num: int) -> str:
        #1:
        if num == 0: return "0"
        ans, rlt = [], ''
        dict_num = {'10':'a', '11':'b', '12':'c', '13':'d', '14':'e', '15':'f'}

        if num < 0:
            num += 0xffffffff + 1

        while (num != 0):
            ans.append(num%16)
            num //= 16

        for i in range(len(ans)-1, -1, -1):
            if ans[i]>=10:
                rlt += dict_num[str(ans[i])]
            else:
                rlt += str(ans[i])

        return (rlt)

s= Solution()
print(s.toHex1(-98), s.toHex2(-98), s.toHex3(-98))