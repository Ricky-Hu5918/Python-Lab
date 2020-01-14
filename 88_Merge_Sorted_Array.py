"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
"""
'''#1: 注意返回列表的长度一定是m+n，超过m+n长度的0元素应该移除'''
def merge(nums1, m, nums2, n):
    def insert_element(nums, num): #在nums1中找到第一个比num大的数，在其前面插入num，成功则计数＋1，否则计数为0
        cts = 0
        for i in range(len(nums)):
            if (nums[i] > num):
                nums.insert(i, num)
                cts += 1
                break
        return cts

    count = 0
    for i in range(n): #遍历nums2，将其插入nums1中，并计数
        count += insert_element(nums1, nums2[i])  #累加插入次数

    for count in range(count, n): #nums2中剩余没有插入nums1的数，说明都比nums1中大，需要从m+count位置直接插入nums1
        nums1.insert(m+count, nums2[count])

    for i in range(len(nums1)-1, -1, -1): #nums1中补0的元素倒序剔除，但要注意最终nums1的长度必须等于m+n
        if (nums1[i] == 0) and (i>=m+n):
            nums1.pop()
        else:
            break

    return nums1

nums1, nums2 = [1,2,0,0,0], [2,5,6]  #[1,2,2,5,6]
m, n= 2, 3

nums3, nums4 = [-1,0,0,3,3,3,0,0,0], [1,2,2]  #[-1, 0, 0, 1, 2, 2, 3, 3, 3]
m3, n3 = 6, 3

nums5, nums6 = [-1,-1,0,0,0,0], [-1,0]
m4, n4 = 4, 2

print(merge(nums5, m4, nums6, n4))