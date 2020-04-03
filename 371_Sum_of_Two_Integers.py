'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = -2, b = 3
Output: 1
'''
'''两个整数a, b; a ^ b是无进位的相加； a&b得到每一位的进位；让无进位相加的结果与进位不断的异或， 直到进位为0；

以上方法没问题，但对于Python来说，由于python整数类型为Unifying Long Integers, 即无限长整数类型，因此对于有符号数，即负数，需要做一个处理。
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask

        while (b):
            carry = (a & b)
            a = a ^ b
            b = (carry << 1) & mask

        return a if a < 0x80000000 else ~(a ^ mask)

    def getSum2(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask

        if (b == 0):
            return a if a < 0x80000000 else ~(a ^ mask)

        carry = (a & b)
        a = a ^ b
        b = (carry << 1) & mask

        return self.getSum2(a, b)


getsum = Solution()
print(getsum.getSum(-10, 2))
print(getsum.getSum2(-10, 2))
