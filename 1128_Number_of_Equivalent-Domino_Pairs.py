'''
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Constraints:
1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
'''
'''思路：把元素排序并映射成哈希表，对出现次数进行组合运算，n * (n - 1) // 2，求其出现的对数，即n个数中成对出现的组合。'''
class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        domi_dict = dict()
        for d1, d2 in dominoes:
            idx = tuple(sorted((d1, d2)))

            if idx in domi_dict:
                domi_dict[idx] += 1
            else:
                domi_dict[idx] = 1

        count = 0
        for v in domi_dict.values():
            count += (v * (v - 1)) // 2

        return count

test = Solution()
dominoes = [[1,2],[2,1],[3,4],[1,2]]
print(test.numEquivDominoPairs(dominoes))