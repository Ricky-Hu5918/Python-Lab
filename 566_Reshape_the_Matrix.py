'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''


class Solution:
    def matrixReshape1(self, nums, r, c):
        ans, tmp = [], []
        for each in nums:
            for item in each:
                tmp.append(item)
                if len(tmp) == c:
                    ans.append(tmp)
                    r -= 1
                    tmp = []

        return ans if r == 0 else nums

    def matrixReshape2(self, nums, r, c):
        if len(nums) == 0 or r*c != len(nums)*len(nums[0]):
            return nums

        ans = [[0 for i in range(c)] for x in range(r)]
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                ans[count//c][count%c] = nums[i][j]
                count += 1

        return ans


test = Solution()
nums, r, c = [[1,2], [3,4]], 1, 4
print(test.matrixReshape2(nums, r, c))
