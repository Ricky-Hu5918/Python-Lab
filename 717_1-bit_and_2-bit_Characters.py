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
        flag_0, falg_1 = False, False
        idx = 0
        while idx < len(bits):
            if (bits[idx] == 0):
                idx += 1
                flag_0, falg_1 = True, False
            else:
                idx += 2
                flag_0, falg_1 = False, True

        return flag_0


test = Solution()
bits = [1,1,0,1,0]  #False
print(test.isOneBitCharacter1(bits))