'''
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false

Constraints:
0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
'''

import collections
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if (not A or not B) or (len(A) != len(B)) or (len(set(A)) != len(set(B))) or (
                collections.Counter(A) != collections.Counter(B)):
            return False

        if (A == B):
            if (len(set(A)) != len(A)):
                return True
            else:
                return False

        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1

        return True if count == 2 else False

test = Solution()
A, B = 'abcaa', 'abcbb'
A1, B1 = 'abab', 'abab'
print(test.buddyStrings(A1,B1))