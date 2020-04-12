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

        '''求负数的补码'''
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

        '''#求负数的补码'''
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

    '''纯手工求补码'''
    def toHex4(self, num: int) -> str:
        if num == 0: return "0"
        ans, rlt = [], ''
        tmp2, tmp3 = '', ''

        # 处理负数（求其补码，即去掉符号，转成二进制，对二进制取反，最后加1得到补码）
        if num < 0:
            tmp = bin(abs(num))[2:]  # 转换成二进制，并取出二进制的数字部分（去掉ob）

            for each in tmp:  # 对二进制部分取反，此时高位部分是全0
                if int(each) == 0:
                    each = '1'
                else:
                    each = '0'
                tmp2 += each

            for i in range(len(tmp2), 32):  # 高位部分补全1，完成取反全过程
                tmp3 += '1'
            tmp2 = tmp3 + tmp2

            num = int('0b' + tmp2, 2) + 1  # 取反后加1，转成十进制，得到负数的补码

        # 对正数进行16进制化处理（包括负数的补码）
        while (num != 0):
            ans.append(num % 16)
            num //= 16

        for i in range(len(ans) - 1, -1, -1):
            if ans[i] >= 10:
                rlt += chr(87 + ans[i])  # a=97
            else:
                rlt += str(ans[i])

        return (rlt)

s= Solution()
print(s.toHex1(-98), s.toHex2(-98), s.toHex3(-98))