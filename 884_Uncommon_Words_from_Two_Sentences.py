'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
'''

import collections
class Solution:
    def uncommonFromSentences1(self, A: str, B: str):
        if not A: return B.split()
        if not B: return A.split()

        A_set = collections.Counter(A.split())
        B_set = collections.Counter(B.split())
        tmp = A_set + B_set

        for k in list(tmp.keys()):
            if tmp[k] >= 2:
                del tmp[k]

        return list(tmp)

    '''# 3:'''
    def uncommonFromSentences3(self, A: str, B: str):
        C = collections.Counter(A.split()) + collections.Counter(B.split())
        return [k for k, v in C.items() if v == 1]

    '''# 2:'''
    def uncommonFromSentences2(self, A: str, B: str):
        C = (A + ' ' + B).split()
        res = []
        for c in C:
            if C.count(c) == 1:
                res.append(c)

        return res


test = Solution()
A, B = "this apple is sweet sweet ", "this apple is super sour"
print(test.uncommonFromSentences1(A, B))