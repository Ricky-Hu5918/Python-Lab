'''
Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Constraints:
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
'''
'''考察各种排序算法，目前仅会：冒泡排序，选择排序，和快速排序'''

'''#1：冒泡排序，timeout'''
def sortArray1(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] > nums[j]):
                nums[i], nums[j] = nums[j], nums[i]

    return nums

'''#2: 选择排序, timeout'''
def sortArray2(nums):
    def find_min_item(arr):
        min_item, min_idx = arr[0], 0
        for i in range(1, len(arr)):
            if min_item > arr[i]:
                min_item = arr[i]
                min_idx = i

        return min_idx

    new_sorted_arr = []
    while (len(nums) != 0):
        idx = find_min_item(nums)
        new_sorted_arr.append(nums.pop(idx))

    return new_sorted_arr

'''#3: 快速排序, passed'''
def sortArray3(nums):
    #base case
    if (len(nums)<2):
        return nums

    #select a pivot
    pivot = nums[0]

    #grouping
    less_list = [each for each in nums[1:] if each < pivot]
    large_list = [each for each in nums[1:] if each >= pivot]

    #recursing
    return sortArray3(less_list) + [pivot] + sortArray3(large_list)

'''#4: 用built-in方法, passed'''
def sortArray4(nums):
    # nums.sort()
    # return nums
    return sorted(nums)

nums = [5,1,1,2,0,0,6,10,-1]
print(sortArray1(nums))
print(sortArray2(nums))
nums1 = [5,1,1,2,0,0,6,10,-1]
print(sortArray3(nums1))