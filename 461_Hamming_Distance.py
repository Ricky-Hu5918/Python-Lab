'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

'''using bin() method, which can convert int into binary'''
class Solution:
    def hammingDistance2(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


    def hammingDistance1(self, x: int, y: int) -> int:
        tmp = x ^ y
        count = 0

        while tmp>0:
            if (tmp & 1) == 1:
                count += 1

            tmp >>= 1

        return count

    '''xk's method'''
    def hammingDistance3(self, x: int, y: int) -> int:
        if x == y:
            return 0
        binx, biny = bin(x)[2:], bin(y)[2:]  #bin()的返回值为字符串‘0bxxxxxx’,因此要去掉前面两个字符
        maxlen = max(len(binx), len(biny))

        # the first zero padding method
        binx, biny = '%0*d' % (maxlen, int(binx)), '%0*d' % (maxlen, int(biny))

        # second zero padding method
        # binx, biny = binx.zfill(maxlen), biny.zfill(maxlen)

        # third (manual) padding method
        # if len(binx) > len(biny):
        #     for k in range(len(binx)-len(biny)):
        #         biny = '0' + biny
        # elif len(biny) > len(binx):
        #     for k in range(len(biny)-len(binx)):
        #         binx = '0' + binx

        count = 0
        for i in range(maxlen):
            if binx[i] != biny[i]:
                count += 1

        return count

x, y = 3, 137
test = Solution()
print(test.hammingDistance1(x,y), test.hammingDistance2(x,y))