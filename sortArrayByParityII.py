#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 922
'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.

Example 1:
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
'''

def sortArrayByParityII(A):
    B = A.copy()
    ou, ji = 0, 1

    '''把A中的偶数放入B中的偶数下标位置，把A中的奇数放入B中奇数下标的位置'''
    for i in range(len(A)):
        if (A[i] % 2 == 0):
            B[ou] = A[i]
            ou += 2
        else:
            B[ji] = A[i]
            ji += 2
    print(B)
    return B

'''#my solution:把偶数和奇数分别存放在B和C中，按照下标的奇偶组合放进D中
        B = []
        C = []
        D = []
        for i in range(len(A)):
            if (A[i]%2 == 0):
                B.append(A[i])
            else:
                C.append(A[i])

        i, k = 0, 0
        for j in range(len(A)):
            if (j%2 == 0): #偶数下标存一个偶数
                D.append(B[i])
                i += 1
            else: #奇数下标存一个奇数
                D.append(C[k])
                k += 1

        return D'''

if __name__ == '__main__':
    A = [4,2,5,7,3,6,9,10]
    sortArrayByParityII(A)
