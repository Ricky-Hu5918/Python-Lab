'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
'''
'''#1: 原本是timeout的'''
def containsNearbyDuplicate(nums, k):
    if (len(set(nums)) == len(nums)): #增加这个判断之后不再timeout
        return False

    for i in range(len(nums)):
        idx  = 1
        while ((i+idx)<len(nums) and (idx <= k)):
            if (nums[i] == nums[i+idx]):
                return True
            idx += 1

    return False

'''#2: 原本是timeout的, 现在96ms'''
def containsNearbyDuplicate2(nums, k):
    if (len(set(nums)) == len(nums)): #增加这个判断之后不再timeout
        return False

    tmp = []
    for item in nums:
        if item not in tmp:
            tmp.append(item)
        else:
            i = tmp.index(item)
            tmp.append(item)
            if (len(tmp[i:])<=k+1):
                return True
            tmp.remove(item)

    return False

nums1, k1 = [9, 9], 2 #true
nums2, k2 = [1,2,3,4,5,6,7,8,9,9], 3 #true
nums3, k3 = [1,2,3,1,2,3], 2 #false
nums4, k4 = [1,0,1,1], 1 #true
print(containsNearbyDuplicate2(nums4, k4))

