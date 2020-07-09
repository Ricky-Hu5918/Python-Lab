'''
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

Example 1:
Input: 22
Output: 2
Explanation:
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.

Example 2:
Input: 5
Output: 2
Explanation:
5 in binary is 0b101.

Example 3:
Input: 6
Output: 1
Explanation:
6 in binary is 0b110.

Example 4:
Input: 8
Output: 0
Explanation:
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
 
Note:
1 <= N <= 10^9
'''

class Solution:
    def binaryGap3(self, N: int) -> int:
        binN = bin(N)[2:]
        count, max_dis = 0, 0
        for n in binN:
            if n == '1':
                if count == 0:
                    count = 1
                else:
                    max_dis = max(max_dis, count)
                    count = 1
            else:
                if count:
                    count += 1

        return max_dis

    # 2:
    def binaryGap2(self, N: int) -> int:
        binN = bin(N)[2:]
        bit1_idx, max_dis = [], 0

        for i, v in enumerate(binN):
            if v=='1':
                bit1_idx.append(i)

        if len(bit1_idx)>1:
            for i in range(len(bit1_idx)-1, -2, -1):
                max_dis = max(max_dis, bit1_idx[i]-bit1_idx[i-1])

        return max_dis

    # 1: using bin() method
    def binaryGap1(self, N: int) -> int:
        binN = bin(N)[2:]
        if (binN).count('1')<=1:
            return 0

        max_dis, bit1_idx = 0, []
        for i in range(len(binN)):
            if binN[i] == '1':
                bit1_idx.append(i)
                if len(bit1_idx) == 2:
                    max_dis = max(max_dis, bit1_idx[1]-bit1_idx[0])
                    bit1_idx.pop(0)

        return max_dis

test = Solution()
N = 810
print(test.binaryGap1(N), test.binaryGap2(N), test.binaryGap3(N))