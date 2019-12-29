"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

'''#1: 常规方法，轮询值为0的元素，执行remove操作，并记录操作次数，最后按照删除次数将0添加到列表。用时180ms'''
def moveZeroes1(nums):
    cts = 0
    i = 0
    while (i < len(nums)):
        print(nums[i])
        if (nums[i] == 0):
            nums.remove(0)
            cts += 1
            i = (i-1) if i>=1 else 0
        else:
            i += 1

    while (cts != 0):
        nums.append(0)
        cts -= 1

    return nums

'''#2: 直接使用remove操作，记录remove次数，发生异常时break，最后按照remove次数将0添加到列表。耗时164ms'''
def moveZeroes2(nums):
    j = 0
    for i in range(len(nums)):
        try:
            nums.remove(0)
            j += 1
        except ValueError:
            break

    while (j != 0):
        nums.append(0)
        j -= 1

    return nums

'''#3: 按照元素0存在的次数进行单次冒泡排序。耗时1604ms'''
def moveZeroes3(nums):
    for k in range(nums.count(0)):
        for i in range(len(nums)-1):
            j = i + 1
            if (nums[i] == 0):
                nums[i], nums[j] = nums[j], nums[i]

    return nums

'''#4: 肖哥的方法，遍历列表，将非零的元素从0位置开始覆盖，剩余位置用0来覆盖. 44ms,效率非常高！！'''
def moveZeroes4(nums):
    none_zero_item = 0
    for each in nums:
        if (each != 0):
            nums[none_zero_item] = each
            none_zero_item += 1

    for i in range(none_zero_item, len(nums)):
        nums[i] = 0

    return nums

nums = [0,1,0,3,12]
nums1 = [0,0,1]
print(moveZeroes4(nums))