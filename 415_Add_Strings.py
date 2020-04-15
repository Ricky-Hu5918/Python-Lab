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

    '''xk's method'''
    def addStrings2(self, num1: str, num2: str) -> str:
        num1, num2 = list(map(int, num1[::-1])), list(map(int, num2[::-1]))
        print(num1, num2)
        if len(num1)<len(num2):
            num1, num2 = num2, num1

        carry = 0
        for i in range(len(num1)):
            if i < len(num2):
                n = num2[i]
            else:
                n = 0

            tmp = n + carry + num1[i]
            num1[i] = tmp%10
            carry = tmp//10

        if carry:
            num1.append(1)

        return ''.join(map(str, num1))[::-1]

    '''参考题解'''
    def addStrings3(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res
        

test = Solution()
num1, num2 = "1111", "999999"   #"1001110"
print(test.addStrings2(num1, num2))