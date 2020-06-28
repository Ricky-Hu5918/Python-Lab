'''
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''


class Solution:
    def shortestToChar2(self, S: str, C: str):
        # 2: xk's method
        res, c_idx = [len(S) for _ in range(len(S))], []

        for i in range(len(S)):
            if S[i] == C:
                c_idx.append(i)

        for i in range(len(res)):
            res[i] = min([abs(c_idx[x] - i) for x in range(len(c_idx))])

        return res

    '''# 1: 分别从左到右和从右到左进行扫描，将各字符相对左C或右C得最小距离记录下来即可。'''
    def shortestToChar1(self, S: str, C: str):
        res = [len(S) for _ in range(len(S))]

        #from left to right
        left = None
        for i in range(len(S)):
            if S[i] == C:
                res[i] = 0
                left = i

            if left != None:
                res[i] = i - left

        #from right to left
        right = None
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                right = i
            elif right != None:
                res[i] = min(res[i], right - i)

        return res

    '''xk's much better solution, still don't understand'''
    def shortestToChar(self, S: str, C: str):
        res = []
        S = ' ' + S
        lMat = 0  # here lMat means: last match
        for i in range(len(S)):
            res.append(i - lMat)
            if S[i] == C:
                if lMat:
                    res[(i + lMat) // 2 + (i + lMat) % 2:] = res[(i + lMat) // 2:lMat - 1:-1]
                else:
                    res[0::1] = res[i::-1]
                print(res)
                lMat = i
        return res[1:]

test = Solution()
S, C = "loveleetcode", 'e'
# print(test.shortestToChar1(S,C), test.shortestToChar2(S,C))
print(test.shortestToChar(S,C))