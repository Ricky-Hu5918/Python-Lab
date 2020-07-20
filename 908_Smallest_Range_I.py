'''
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

Example 1:
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:
Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]

Note:
1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
'''

'''题意：返回A中最大值的最小值-A中最小值的最大值'''
class Solution:
    def smallestRangeI(self, A, K: int) -> int:
        A.sort()
        return 0 if (A[0]+K) >= (A[-1]-K) else (A[-1]-K)-(A[0]+K)

test = Solution()
A, K = [1,3,6], 3
print(test.smallestRangeI(A,K))