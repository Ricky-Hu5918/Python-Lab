'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
'''


class Solution:
    def numMagicSquaresInside(self, grid) -> int:
        row, col, count = 0, 0, 0
        check_sum = sum([i for i in range(1, 10)]) // 3

        while ((row + 3) <= len(grid)):
            while (col + 3) <= len(grid[0]):
                check_square = set()
                for r in range(row, row + 3):
                    r_sum = 0
                    for c in range(col, col + 3):
                        if grid[r][c] <= 9 and grid[r][c] >= 1:
                            check_square.add(grid[r][c])
                            r_sum += grid[r][c]
                    if r_sum != check_sum:
                        break

                if (len(check_square) == 9) and \
                        (sum([grid[row][col], grid[row + 1][col + 1], grid[row + 2][col + 2]]) == check_sum) and \
                        (sum([grid[row][col], grid[row + 1][col], grid[row + 2][col]]) == check_sum):
                    count += 1

                col += 1

            row += 1
            col = 0

        return count

test = Solution()
grid = [[4,7,8],[9,5,1],[2,3,6]]
print(test.numMagicSquaresInside(grid))