"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
"""

'''#1: 常规方法，先找到needle的第一个元素，然后切片比较是否等于needle'''
def strStr(haystack, needle):
    if not needle:
        return 0

    if not haystack:
        return -1

    len_needle, len_haystack = len(needle), len(haystack)
    if (len_needle > len_haystack):
        return -1

    for i in range(len_haystack):
        if (needle[0] == haystack[i]):
            if (haystack[i:(i + len_needle)] == needle):
                return i

        if (i == len_haystack - 1):
            return -1

'''#2: 代码长度增加，但是效率有所提高'''
def strStr2(haystack, needle):
    if not needle:
        return 0

    if not haystack:
        return -1

    len_needle, len_haystack = len(needle), len(haystack)
    if (len_needle > len_haystack):
        return -1

    idx, count = 0, 0
    while (idx < len_haystack):
        if (haystack[idx] == needle[0]):
            if (len_haystack-1-idx >= len_needle-1):
                for i in range(1, len_needle):
                    if (haystack[idx+i] == needle[i]):
                        count += 1
                    else:
                        count = 0
                        break

                if (count+1 == len_needle):
                    return idx
            else:
                return -1
        idx += 1

    return -1

'''#3: 使用find方法，一行搞定！但没什么意义，还是要尽量少用系统自带的函数。'''
def strStr3(haystack, needle):
    return haystack.find(needle)

'''#4: sunday算法'''
def strStr4(haystack, needle):
    # Func: 计算偏移表
    #偏移表的作用是存储每一个在 needle 中出现的字符，在 needle 中出现的最右位置到尾部的距离 +1
    def calShiftMat(st):
        dic = {}
        for i in range(len(st) - 1, -1, -1):
            if not dic.get(st[i]):
                dic[st[i]] = len(st) - i
        dic["ot"] = len(st) + 1
        return dic

    if not needle: return 0
    if not haystack: return -1

    idx = 0
    len_needle, len_haystack = len(needle), len(haystack)
    if (len_needle > len_haystack): return -1
    # 偏移表预处理
    dic = calShiftMat(needle)
    while (idx+len_needle <= len_haystack):
        str_cut = haystack[idx:idx+len_needle]
        if (str_cut == needle):
            return idx
        else:
            if (idx + len_needle >= len_haystack): # 边界处理
                return -1

            cur_c = haystack[idx + len_needle] # 不匹配情况下，根据下一个字符的偏移，移动idx
            print('cur_c', cur_c)
            if dic.get(cur_c):
                idx += dic[cur_c]
                print('curc_idx', dic[cur_c], idx)
            else:
                idx += dic["ot"]
                print('idx', idx)

    return -1 if idx+len_needle >= len_haystack else idx


haystack, needle = "hello", "ll"
haystack1, needle1 = "aaaba", "baa"
haystack2, needle2 = "babba", "bba"
haystack3, needle3 = "babaa", "baa"
haystack4, needle4 = "bbaabab", "baa"
haystack5, needle5 = "checkouthisout", "this"
print(strStr4(haystack5, needle5))