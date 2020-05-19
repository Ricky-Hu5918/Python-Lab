'''
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.
Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.
Note:

The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].
'''

'''分几种情况进行总结归纳，得到结论后进行普适性编码'''
'''1：种类大于总数的一半，最多只能拿到总数一半的糖果种类；2：种类小于总数的一半，可以拿到所有种类的糖果'''
class Solution:
    def distributeCandies2(self, candies):
        return min(len(set(candies)), len(candies) // 2)

    """    # 1:"""
    def distributeCandies1(self, candies):
        total_num = len(candies)
        kinds_num = len(set(candies))

        if (total_num//2) >= kinds_num:
            return kinds_num
        else:
            return total_num//2

test = Solution()
candies = [1, 2, 3, 3]
print(test.distributeCandies1(candies), test.distributeCandies2(candies))