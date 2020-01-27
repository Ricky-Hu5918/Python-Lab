"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.
Note: Each term of the sequence of integers will be represented as a string.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
"""

'''#1: xk's normal solution'''
def countAndSay(n):
    base_str = '1'
    if n == 1:
        return base_str

    count_loop = 1
    while (count_loop < n):
        idx_i, idx_j = 0, 0
        count, tmp_str = 0, ''

        while (idx_j < len(base_str)):
            if (base_str[idx_i] != base_str[idx_j]):
                tmp_str += str(count) + str(base_str[idx_i])
                count = 0
                idx_i = idx_j
            else:
                count += 1
                idx_j += 1

        if count > 0:
            tmp_str += str(count) + str(base_str[idx_i])

        base_str = tmp_str
        count_loop += 1
        print(count_loop, base_str)

    return base_str


n1 = 1 #1
n2 = 2 #11
n3 = 3 #21
n4 = 4 #1211
n5 = 5 #111221
n6 = 6 #312211
n7 = 7 #13112221
print(countAndSay(n4))