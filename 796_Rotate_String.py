'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
'''
'''#思路：只需比较一下两个字符串的长度，然后判断A + A中是否存在B就ok，因为A + A中已经包含了所有可能的移动情况'''
class Solution:
    def rotateString1(self, A: str, B: str) -> bool:
        return (B in A*2) if len(A)==len(B) else False

    '''将字符串 A 旋转 s 次后，得到的字符串为 A[s], A[s + 1], A[s + 2], ...，
    因此我们只要枚举 s，并检查是否有 A[s] == B[0], A[s + 1] == B[1], A[s + 2] == B[2], ... 即可。'''
    def rotateString2(self, A, B):
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for s in range(len(A)):
            if all(A[(s+i) % len(A)] == B[i] for i in range(len(A))):
                return True
        return False

test = Solution()
A, B = 'abcde', 'cdeab'
print(test.rotateString1(A, B), test.rotateString2(A,B))