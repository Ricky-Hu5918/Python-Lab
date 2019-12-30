"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Example 1:

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move. 
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 
Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
"""

'''#1: 92ms, not that good'''
def removeDuplicates(S):
    res, resS = [], ''
    res.append(S[0])

    for i in range(1, len(S)):
        if (not res):
            res.append(S[i])
        else:
            if (S[i] == res[-1]):
                res.pop()
            else:
                res.append(S[i])

    for each in res:
        resS += each

    return resS

'''#2: 152ms, not good'''
def removeDuplicates2(S):
    S_list = list(S)
    i, S_str = 0, ''

    while (i < len(S_list)-1):
        if (S_list[i] == S_list[i+1]):
            S_list.pop(i)
            S_list.pop(i)
            i = i-1 if i>=1 else 0
        else:
            i += 1

    for each in S_list:
        S_str += each

    return S_str

'''#3: xk's recursion version 1. timeout timeout but it's worth learning'''
def removeDuplicates3(S):
    if (len(S) <= 1):
        return S

    list_S = list(S)
    for i in range(len(list_S)-1):
        if (list_S[i] == list_S[i+1]):
            list_S.pop(i)
            list_S.pop(i)
            return removeDuplicates3(''.join(list_S))

    return S

'''#4: xk's recursion version 2. timeout but it's worth learning'''
def removeDuplicates4(S):
    if (len(S) <= 1):
        return S

    for i in range(len(S)-1):
        if (S[i] == S[i+1]):
            S = S[:i] + S[i:].replace(S[i], '', 2)
            print(S)
            return removeDuplicates3(S)

    return S

S = "abbaca"  #ca
S1 = "aababaab"  #"ba"
print(removeDuplicates4(S1))