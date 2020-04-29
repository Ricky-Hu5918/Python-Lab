'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
'''


class Solution:
    def findComplement3(self, num: int) -> int:
    #3: #所谓补数，就是原值与FF的异或
        tmp = num
        i = 0
        while tmp:
            tmp >>= 1
            i = (i << 1) + 1
        return num^i

    '''# 2: treated it as a string'''
    def findComplement2(self, num: int) -> int:
        tmp = bin(num)[2:]

        tmp = tmp.replace('1', 'x')
        tmp = tmp.replace('0', '1')
        tmp = tmp.replace('x', '0')

        return int('0b'+tmp, 2)

    '''#1: normal way'''
    def findComplement1(self, num: int) -> int:
        ans = ''
        while num>0:
            ans += str(0) if ((num)&1) else str(1)
            num >>= 1

        return int('0b'+ ans[::-1], 2)