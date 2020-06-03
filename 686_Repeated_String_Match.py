'''
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
'''

class Solution:
    def repeatedStringMatch1(self, A: str, B: str) -> int:
        if len(B)<=len(A) and not set(B).issubset(set(A)):
            return -1

        if len(B)>len(A) and not set(B).issubset(set(A)):
            return -1

        count = 2
        while (B not in A):
            tmp = A*count
            if B in tmp: return count
            if (len(tmp)>2*len(B)): return -1
            count += 1

        return 1


test = Solution()
A1, B1 = "aaaaaaaaaaaaaaaaaaaaaab", "ba"  #2
A2, B2 = "abcabcabcabc", "abac"  #-1
print(test.repeatedStringMatch1(A1, B1))
print(test.repeatedStringMatch1(A2, B2))