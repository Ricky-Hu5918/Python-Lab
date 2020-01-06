
'''
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called
a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + … + A[Q].
Write a function:
def solution(A)
that, given an array A consisting of N integers, returns the maximum sum of any slice of A.
For example, given array A such that:
A[0] = 3 A[1] = 2 A[2] = -6 A[3] = 4 A[4] = 0
the function should return 5 because:
(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
'''


def max_slice(arr):
    global_max = arr[0]
    local_max = arr[0]
    for i in range(1, len(arr)):
        temp_sum = local_max + arr[i]
        if temp_sum > arr[i]:
            local_max = temp_sum
            if local_max > global_max:
                global_max = local_max
        else:
            local_max = arr[i]

    return global_max

def maximum_slice(A):
    if not A:
        return 0

    temp_max, global_max = A[0], A[0]
    for i in range(1, len(A)):
        temp = temp_max + A[i]
        if temp > A[i]:
            temp_max = temp
            if temp_max > global_max:
                global_max = temp_max
        else:
            temp_max = A[i]

    return global_max

arr1 = [5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3]
arr2 = [1,2,3,-8,5,6]
print(maximum_slice(arr1))
print(max_slice(arr1))