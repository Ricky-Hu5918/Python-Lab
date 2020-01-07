"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
'''#1:常规方法，复杂度高，效率低！
思路：先把第一个和第二个元素中相同部分取出来作为样板，再将后续的元素与样板对比，不在样板中的就剔除'''
def longestCommonPrefix1(strs):
    if (len(strs) == 1):
        return strs[0]

    if not strs:
        return ''

    prefix_stack = []
    for i in range(min(len(strs[0]), len(strs[1]))):
        if (strs[0][i] == strs[1][i]):
            prefix_stack.append(strs[0][i])  #把样板列表造出来
        else:
            if (i == 0):
                return ''

    for each in strs[2:]:
        if not each:
            return ''

        for i in range(len(prefix_stack)):
            if (each[i] != prefix_stack[i]):
                if (i == 0):
                    return ''
                else:
                    if (i+1 <= len(prefix_stack)): #不在样板中，且长度小于样板长度，剔除
                        for j in range(i, len(prefix_stack)):
                            prefix_stack.pop()
                        break

            if (i == len(each)-1): #在样板中，但元素长度小于样板长度
                for j in range(i+1, len(prefix_stack)):
                    prefix_stack.pop()
                break

    return ''.join(prefix_stack)

'''#2: #1的优化版本，直接将第一个元素作为样板'''
def longestCommonPrefix2(strs):
    if not strs:
        return ''

    res = list(strs[0])

    for each in strs[1:]:
        if not each:
            return ''
        for i in range(len(res)):
            if (each[i] != res[i]):
                if (i == 0):
                    return ''
                else:
                    if (i+1<=len(res)):
                        for j in range(i, len(res)):
                            res.pop()
                        break

            if (i == len(each)-1): #在样板中，但元素长度小于样板长度
                for j in range(i+1, len(res)):
                    res.pop()
                break

    return ''.join(res)

'''#3: 肖哥的思路：找到元素的最小长度，以此作为切片长度进行轮询'''
def longestCommonPrefix3(strs):
    if not strs:
        return ''

    len_min_str = len(strs[0])
    for each in strs[1:]:
        len_min_str = min(len_min_str, len(each))

    if (len_min_str == 0):
        return ''

    idx = 0
    while (idx < len_min_str):
        for item in strs[1:]:
            if (item[idx] != strs[0][idx]):  #关键点
                return strs[0][:idx]
        idx += 1

    return strs[0][:idx]

'''#4: 老刘的zip方法'''
def longestCommonPrefix4(strs):
    if (len(strs) == 1):
        return strs[0]

    if not strs:
        return ''

    result = list(zip(*(list(str2) for str2 in strs)))
    if not result:
        return ''
    print(result)
    rt_str = ''
    for i in range(len(result)):
        if(len(set(result[i])) != 1):
            break
        else:
            rt_str += result[i][0]

    return rt_str

strs = ["abab","aba",""]
strs1 = ["a","a","a"]
strs2 = ["acce","acce","acc","accr"]
strs3 = ['a']
strs4 = ['ac', 'ac', 'a', 'a']
strs5 = []
strs6 = ["abca","aba","aaab"]
print(longestCommonPrefix4(strs6))