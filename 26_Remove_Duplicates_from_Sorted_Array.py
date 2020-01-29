"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
"""
'''#1: A normal version'''
def removeDuplicates1(nums):
    idx = 0
    while idx < len(nums)-1:
        if (nums[idx] == nums[idx+1]):
            nums.pop(idx)
            idx -= 1 if idx>=1 else 0
        else:
            idx += 1

    return len(nums)

'''#2: Same as #1, but it is better'''
def removeDuplicates2(nums):
    pre, cur = 0, 1
    while cur < len(nums):
        if (nums[pre] == nums[cur]):
            nums.pop(cur)
        else:
            pre, cur = pre+1, cur+1

    return len(nums)

'''#3: xk's version, but I do not use reverse function'''
def removeDuplicates3(nums):
    ll, pre, count = len(nums), nums[0], 1
    nums.append(pre)

    idx = 0
    while (idx < ll):
        if (pre != nums[idx]):
            nums.append(nums[idx])
            count += 1
        pre = nums[idx]
        idx += 1

    for i in range(count):
        nums[i] = nums[ll+i]

    for i in range(ll):
        nums.pop()

    return len(nums)

'''#4: xk's version'''
def removeDuplicates4(nums):
    pre, idx = '', 0

    for each in nums:
        if (pre != each):
            pre = each
            nums[idx] = each
            idx += 1

    return idx

'''#5: lj's version'''
def removeDuplicates5(nums):
    pre, cur = 0, 1

    while (cur < len(nums)):
        if (nums[pre] != nums[cur]):
            nums[pre+1] = nums[cur]
            pre += 1
            cur += 1
        else:
            cur += 1

    return pre+1

nums1 = [0,0,0,1]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates4(nums))