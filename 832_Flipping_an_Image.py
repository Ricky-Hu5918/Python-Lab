'''
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
'''

class Solution:
    def flipAndInvertImage3(self, A):
    #3:
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = 1 - A[i][j]
            A[i] = A[i][::-1]

        return A

    #2: no more space needed
    def flipAndInvertImage2(self, A):
        for i in range(len(A)):
            A[i] = A[i][::-1]
            for j in range(len(A[i])):
                A[i][j] = 0 if A[i][j] else 1

        return A

    #1:
    def flipAndInvertImage1(self, A):
        ans = []
        for a in A:
            a = a[::-1]
            for i in range(len(a)):
                a[i] = 0 if a[i] else 1
            ans.append(a)

        return ans

test = Solution()
A = [[1,1,0],[1,0,1],[0,0,0]]
# print(test.flipAndInvertImage1(A))
#print(test.flipAndInvertImage2(A))
print(test.flipAndInvertImage3(A))