'''
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
 

Note:  1 <= S.length <= 1000
'''

'''在字符串末尾添加一个哨兵字符，可解决连续字母在最后的特殊情况'''
class Solution:
    def largeGroupPositions2(self, S: str):
        # 2: two pointers, same as #1
        idx1, idx2 = 0, 1
        res = []
        S = S + '$'
        while idx2 < len(S):
            if (S[idx1] != S[idx2]):
                if idx2 - idx1 > 2:
                    res.append([idx1, idx2 - 1])
                idx1 = idx2
            idx2 += 1

        # 处理连续字母在最后面的情况
        # if idx2-idx1>2:
        #     res.append([idx1, idx2-1])

        return res

    # 1: normal way
    def largeGroupPositions1(self, S: str):
        count, res, tmp = 0, [], 0

        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                count += 1
                if count == 1: tmp = i
            else:
                if count>=2:
                    res.append([tmp, i])
                count = 0

        #处理整个字符串全为连续字母或末尾为连续字母的情况
        if count>=2:
            res.append([tmp, i+1])

        return res

    '''题解方法，巧妙的化解了末尾连续字符的情况，也没有使用哨兵字符'''
    def largeGroupPositions(self, S: str):
        ans = []
        i = 0 # The start of each group
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans

test = Solution()
S = "abcdddeeeeaabbbcddd"
print(test.largeGroupPositions1(S), test.largeGroupPositions2(S), test.largeGroupPositions(S))