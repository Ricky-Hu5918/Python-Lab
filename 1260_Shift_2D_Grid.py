"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
"""
'''#1: A normal way to address this issue.'''
def shiftGrid(grid, k):
    tmp = []
    for each in grid:
        for i in range(len(grid)):
            tmp.append(each[i])

    res = tmp.copy()
    for i in range(len(tmp)):
        res[(i+k)%len(tmp)] = tmp[i]

    k = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = res[k]
            k += 1

    return grid


grid, k = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1
print(shiftGrid(grid, k))