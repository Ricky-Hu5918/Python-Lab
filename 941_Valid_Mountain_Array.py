'''
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i< A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true

Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000
'''


class Solution:
    def validMountainArray(self, A) -> bool:
        if len(A) <= 2: return False
        mountain_idx = A.index(max(A))
        if (mountain_idx == len(A) - 1) or (mountain_idx == 0):
            return False

        for i in range(mountain_idx):
            if A[i] >= A[i + 1]:
                return False

        for i in range(mountain_idx, len(A) - 1):
            if A[i] <= A[i + 1]:
                return False

        return True

    '''先上山再下山，满足要求的话走的步数应该等于数组长度'''
    def validMountainArray2(self, A) -> bool:
        N = len(A)
        i = 0

        '''walk up until reach the mountain'''
        while i+1<N and A[i]<A[i+1]:
            i += 1

        if i == 0 or i == N-1:
            return False

        '''walk down from the mountain to the end of the array'''
        while i+1<N and A[i]>A[i+1]:
            i += 1

        return i == N-1

test = Solution()
A = [0,1,3,2,1,2]
print(test.validMountainArray(A), test.validMountainArray2(A))
