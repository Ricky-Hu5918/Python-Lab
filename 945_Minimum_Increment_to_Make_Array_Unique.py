'''
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

Example 1:
Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:
Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
'''

'''#1: normal way'''
def minIncrementForUnique(A):
    if not A: return 0

    A.sort()
    A_base, count = A[0], 0
    for i in range(1, len(A)):
        if (A[i]<=A_base):
            count += (A_base - A[i]) + 1
            A[i] = A_base + 1

        A_base = A[i]

    return count

A1 = [0,2,2,2,2]  #6
A2 = [3,2,1,2,1,7]  #6
print(minIncrementForUnique(A2))