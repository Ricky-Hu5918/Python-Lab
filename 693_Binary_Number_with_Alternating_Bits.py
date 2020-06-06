'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101

Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.

Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.

Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
'''

class Solution:
    def hasAlternatingBits3(self, n: int) -> bool:
        '''# 3:'''
        while n:
            if ((n & 0x3 == 1) or (n & 0x3 == 2)):
                n >>= 1
            else:
                return False

        return True

    '''# 2: same as #1'''
    def hasAlternatingBits2(self, n: int) -> bool:
        bin_n = ''
        while n:
            bin_n += str(n&1)
            n >>= 1

        return ("00" not in bin_n) and ("11" not in bin_n)

    '''# 1: using bin() method'''
    def hasAlternatingBits1(self, n: int) -> bool:
        return ("00" not in bin(n)) and ("11" not in bin(n))

    '''xk's method'''
    def hasAlternatingBits0(self, n: int) -> bool:
        if n <= 2: return True

        base = n & 1
        while n:
            n >>= 1
            if base == (n & 1):
                return False
            base = (n & 1)

        return True

test = Solution()
print(test.hasAlternatingBits1(90), test.hasAlternatingBits3(26))