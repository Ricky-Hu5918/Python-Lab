'''
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Example 1:
Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
'''
'''#1: normal solution'''
def canThreePartsEqualSum(A):
    if (sum(A) % 3 != 0):
        return False

    base = sum(A) // 3
    tmp, tmp_list = 0, []
    for i in range(len(A)):
        tmp += A[i]
        if tmp == base:
            tmp_list.append(i)
            tmp = 0

    # print(tmp_list)
    return True if len(tmp_list) >= 3 else False

A1 = [0,2,1,-6,6,-7,9,1,2,0,1] #true
A2 = [0,2,1,-6,6,7,9,-1,2,0,1] #false
A3 = [10,-10,10,-10,10,-10,10,-10]  #true
print(canThreePartsEqualSum(A3))