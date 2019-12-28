"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""
'''#1: using Counter method. 48ms'''
from collections import Counter
def intersect1(nums1, nums2):
    res = []
    # 利用Counter()方法统计每个元素在原列表中出现的次数，并做&运算，得到元素出现次数的最小值
    cts = Counter(nums1) & (Counter(nums2))

    for k, v in cts.items(): #遍历字典，将出现次数大于1的元素再次添加
        while v != 0:
            res.append(k)
            v -= 1

    return res

'''#2: normal method. 84ms'''
def intersect2(nums1, nums2):
    res = []
    for i in range(len(nums1)):
        if (nums1[i] in nums2):
            res.append(nums1[i])
            nums2.remove(nums1[i])

    return res

'''#3: normal method. 80ms'''
def intersect3(nums1, nums2):
    nums_set = set(nums1) & set(nums2) #先用set()方法求出二者的合集
    res = list(nums_set).copy()

    for each in list(nums_set):
        cts = min(nums1.count(each), nums2.count(each)) #取出合集中元素在两个列表中出现的最小次数
        while (cts != 1): #次数大于1次的，需要再次添加
            res.append(each)
            cts -= 1

    return res

'''#4: xk's method. Perfect!!!'''
def intersect4(nums1, nums2):
    dict_nums1, dict_nums2, res = {}, {}, []

    for item in nums1:  #将nums1中的元素与其出现次数组成字典
        dict_nums1[item] = dict_nums1.get(item, 0) + 1

    for item in nums2:  #将nums2中的元素与其出现次数组成字典
        dict_nums2[item] = dict_nums2.get(item, 0) + 1

    for k, v in dict_nums1.items(): #遍历nums1的字典
        if dict_nums2.get(k):  #如果nums1字典中的元素在nums2的字典中，则.get()返回其在nums2字典中的次数，否则返回0
            for i in range(min(v, dict_nums2.get(k))): #将同时存在于两个字典中的元素，按最小的重复次数添加到返回列表
                res.append(k)

    return res

'''#5: xk's another version. Also perfect!!!'''
'''思路：将两个数组排序，利用两指针遍历比较两个数组中的元素，相等的元素放入返回列表。由于数组中的元素已经排序了，所以可以按照大小逐个移动指针。'''
def intersect5(nums1, nums2):
    nums1.sort()
    nums2.sort()
    p1, p2, res = 0, 0, []

    while (p1<len(nums1)) and (p2<len(nums2)):
        if (nums1[p1] < nums2[p2]):
            p1 += 1
        elif (nums1[p1] > nums2[p2]):
            p2 += 1
        else:
            res.append(nums1[p1])
            p1 += 1
            p2 += 1

    return res

nums1, nums2 = [1,2,2,1], [2,2]
nums3, nums4 = [4,9,5], [9,4,9,8,4]
nums5 = [54,93,21,73,84,60,18,62,59,89,83,89,25,39,41,55,78,27,65,82,94,61,12,38,76,5,35,6,51,48,61,0,47,60,84,9,13,28,38,21,55,37,4,67,64,86,45,33,41]
nums6 = [17,17,87,98,18,53,2,69,74,73,20,85,59,89,84,91,84,34,44,48,20,42,68,84,8,54,66,62,69,52,67,27,87,49,92,14,92,53,22,90,60,14,8,71,0,61,94,1,22,84,10,55,55,60,98,76,27,35,84,28,4,2,9,44,86,12,17,89,35,68,17,41,21,65,59,86,42,53,0,33,80,20]
print(intersect5(nums1, nums2))
