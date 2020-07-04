'''
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
 

Constraints:

2 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
'''

'''same as #821'''
'''思路：分别从左和从右进行遍历，获取空座位与1的最小相对位置，并存入列表中，列表中最大值即为离最近的人的最远距离'''
class Solution:
    def maxDistToClosest1(self, seats) -> int:
        ll = len(seats)
        res = [ll for _ in range(ll)]

        left = None
        for i in range(ll):
            if seats[i] == 1:
                res[i] = 0
                left = i

            if left != None:
                res[i] = i - left

        right = None
        for j in range(ll - 1, -1, -1):
            if seats[j] == 1:
                right = j

            if right != None:
                res[j] = min(res[j], right - j)
        print(res)
        return max(res)

test = Solution()
seats = [1,0,0,0,1,0,1]  #空座位与1相对位置列表为[0, 1, 2, 1, 0, 1, 0]
print(test.maxDistToClosest1(seats))