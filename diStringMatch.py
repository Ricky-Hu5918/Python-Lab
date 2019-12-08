#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 942
'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 
Example 1:
Input: "IDID"
Output: [0,4,1,3,2]
'''

def diStringMatch(S):
    A = []
    lo, hi = 0, len(S)
    for i in range(len(S)):
        if S[i] == "I":
            A.append(lo)
            lo += 1
        else:
            A.append(hi)
            hi -= 1
    return A + [lo]

if __name__ == '__main__':
    S = "IDID"
    print(diStringMatch(S))