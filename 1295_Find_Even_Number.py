"""
Given an array nums of integers, return how many of them contain an even number of digits.
Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.
 
Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""

'''#1: low level solution.'''
def findEvenNumbers1(nums):
    cts = 0
    for each in nums:
        if (each >= 10) and (each <= 99):
            cts += 1
        elif (each >= 1000) and (each <= 9999):
            cts += 1
    return cts

'''#2: same as #1， not very good.'''
def findEvenNumbers2(nums):
    cts = 0
    for each in nums:
        if (each//10 >= 1) and (each//10 <= 9):
            cts += 1
        elif (each//1000 >=1) and (each//1000 <=9):
            cts += 1
    return cts

'''#3: just so so.'''
def findEvenNumbers3(nums):
    cts = 0
    for each in nums:
        tmp = 0
        while (each != 0):
            each = each // 10
            tmp += 1
        if (tmp%2 == 0):
            cts += 1
    return cts

'''#4: 将整数转成字符串，计算字符串中字符的长度个数即可。'''
def findEvenNumbers4(nums):
    return sum(1 for item in nums if (len(str(item)) % 2 == 0))

'''#5: 思路一样，都是转成字符串，但是效率比#4高一些'''
def findEvenNumbers5(nums):
    odd_count = 0
    for item in nums:
        odd_count += len(str(item))%2
    return len(nums)-odd_count

nums = [12, 345, 2, 6, 7896]  #2
print(findEvenNumbers5(nums))