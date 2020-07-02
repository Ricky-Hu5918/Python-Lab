'''
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.
'''

'''思路：沿着x轴和y轴分别考虑，反向用排除法，正向就确保它们在x和y轴同时存在一段相同线段'''
class Solution:
    def isRectangleOverlap2(self, rec1, rec2) -> bool:
        '''# 2: 排除法，排除所有不可能产生intersection的情况'''
        if (rec1[2] <= rec2[0]) or (rec1[0] >= rec2[2]) or (rec1[3] <= rec2[1]) or (rec1[1] >= rec2[3]):
            return False

        return True

    '''#1: x方向top-right的最小值与bottom-left的最大值之差大于0，并且y方向亦如此的话，那这两个rectangle就是有intersection'''
    def isRectangleOverlap1(self, rec1, rec2) -> bool:
        if ((min(rec1[2], rec2[2])-max(rec1[0], rec2[0]))>0 and ((min(rec1[3], rec2[3])-max(rec1[1], rec2[1]))>0)):
            return True

test = Solution()
rec1, rec2 = [0,0,2,2], [1,1,3,3]
print(test.isRectangleOverlap1(rec1, rec2), test.isRectangleOverlap2(rec1, rec2))