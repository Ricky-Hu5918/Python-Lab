'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def addStrings1(self, num1: str, num2: str) -> str:
        dict_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        # dict_num = dict()
        # for i in range(10):
        #     dict_num[str(i)] = i

        len_num1, len_num2 = len(num1) - 1, len(num2) - 1
        carry, ans = 0, ''
        while (len_num1 >= 0) or (len_num2 >= 0):
            tmp = carry + (dict_num[num1[len_num1]] if len_num1 >= 0 else 0) + \
                  (dict_num[num2[len_num2]] if len_num2 >= 0 else 0)

            if tmp >= 10:
                carry = 1
                tmp = tmp % 10
            else:
                carry = 0
            ans += str(tmp)
            len_num1 -= 1
            len_num2 -= 1

        if carry:
            ans += str(carry)

        return ans[::-1]


test = Solution()
num1, num2 = "1111", "999999"   #"1001110"
print(test.addStrings1(num1, num2))