'''
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
'''


class Solution:
    def isOneBitCharacter1(self, bits) -> bool:
        flag = False
        idx = 0
        while idx < len(bits):
            if (bits[idx] == 0):
                idx += 1
                flag = True
            else:
                idx += 2
                flag = False

        return flag

    '''#2: 如果倒数第二个是0的话，一定是True；其它情况下则判断最后一个0前面连续1的个数，偶数则为True，奇数则为False'''
    def isOneBitCharacter2(self, bits) -> bool:
        count = 0
        idx = len(bits) - 2
        while (idx >= 0) and (bits[idx] == 1):
            count += 1
            idx -= 1

        return (count % 2 == 0)



test = Solution()
bits = [1,1,0,1,0,0]  #True
print(test.isOneBitCharacter1(bits), test.isOneBitCharacter2(bits))