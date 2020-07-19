'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 
Note:
1 <= A.length <= 5000
0 <= A[i] <= 5000
'''

class Solution:
    def sortArrayByParity3(self, A):
        '''# 3: 普通，没有使用额外空间'''
        i = 0
        for j in range(len(A)):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1

        return A

    '''同#1，使用了额外空间'''
    def sortArrayByParity22(self, A):
        return [i for i in A if i % 2 == 0] + [i for i in A if i % 2 != 0]

    '''# 2: 快速排序，递归，太冗余了'''
    def sortArrayByParity2(self, A):
        def quickSort(arry):
            if len(arry)<2:
                return arry
            else:
                pivot = arry[0]
                left = [i for i in arry[1:] if i%2 == 0]
                right = [i for i in arry[1:] if i%2 != 0]

            return quickSort(left) + [pivot] + quickSort(right)

        return quickSort(A)

    '''# 1: 普通，使用了额外空间'''
    def sortArrayByParity1(self, A):
        even, odd = [], []

        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)

        return even+odd

test = Solution()
A = [0,3,5,2,9]
print(test.sortArrayByParity1(A), test.sortArrayByParity2(A), test.sortArrayByParity3(A))