"""
An integer M and a non-empty zero-indexed array A consisting of N non-negative integers are given.
All integers in array A are less than or equal to M.
A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of
the elements A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers.
That is, no individual number occurs more than once in the slice.
For example, consider integer M = 6 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and
(4, 4).
The goal is to calculate the number of distinct slices.
Write a function:
int solution(int M, int A[], int N);
that, given an integer M and a non-empty zero-indexed array A consisting of N integers, returns the number
of distinct slices.
If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.
For example, given integer M = 6 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.
http://www.martinkysel.com/codility-countdistinctslices-solution/
Using the caterpillar method I expand the caterpillar to the right as long as a duplicate element is found.
The right side has to retract as long as this duplicate element has been eliminated from the next slice.
An observation showed that the number of sub-slices is equal to front-back+1.
"""
'''#1: 思路：将元素逐个添加到list中，不出现重复则count加1，出现重复则break'''
def count_distinct_slices(nums, m):
    slices_counts = 0

    ll = len(nums)
    slices_counts += ll
    for i in range(ll-1):
        tmp_list = []
        for j in range(i+1, ll):
            tmp_list.append(nums[i])
            if (nums[j] not in tmp_list):
                tmp_list.append(nums[j])
                slices_counts += 1
            else:
                break

    return slices_counts if slices_counts <= 10**9 else 10**9

'''#2: 肖哥的方法, caterpillar algorithm, 又称毛毛虫算法！没搞懂，:('''
def count_disctinct_slices(m, nums):
    total_slices = 0
    in_current_slice = [False] * (m+1)

    head = 0
    for tail in range(0, len(nums)):
        while head < len(nums) and (not in_current_slice[nums[head]]):
            in_current_slice[nums[head]] = True
            print(head,tail, in_current_slice)
            total_slices += (head - tail) + 1
            head += 1
            total_slices = 1000000000 if total_slices > 1000000000 else total_slices
        in_current_slice[nums[tail]] = False

    print('last', head, tail, in_current_slice)
    return total_slices


nums1 = [2, 4, 1, 7, 4, 9, 7, 3, 5, 5, 8, 7, 1] #m=9, slices=39
nums2 = [3, 4, 5, 5, 2] #m=6, slices=9

print(count_distinct_slices(nums2, 6))
print(count_disctinct_slices(6, nums2))