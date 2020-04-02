'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''
'''#1: 先找到vowel元素在字符串中的index，然后操作字符串进行前后调换顺序'''
def reverseVowels1(s):
    list_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    reverse_idx = []

    for i, j in enumerate(s): #find idx of vowels elements
        if j in list_vowels:
            reverse_idx.append(i)

    if not reverse_idx: return s

    list_s = list(s)
    ll = len(reverse_idx)
    tmp = (ll//2)
    idx = 0
    while (tmp != 0):
        list_s[reverse_idx[idx]], list_s[reverse_idx[ll-1-idx]] = \
            list_s[reverse_idx[ll-1-idx]], list_s[reverse_idx[idx]]
        idx += 1
        tmp -= 1

    return ''.join(list_s)


'''#2: two point'''
def reverseVowels2(s):
    list_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    list_s = list(s)
    left_idx, right_idx = 0, len(s) - 1

    while (left_idx <= right_idx):
        if (list_s[left_idx] not in list_vowels):
            left_idx += 1

        if (list_s[right_idx] not in list_vowels):
            right_idx -= 1

        if (list_s[left_idx] in list_vowels) and (list_s[right_idx] in list_vowels):
            list_s[left_idx], list_s[right_idx] = list_s[right_idx], list_s[left_idx]
            left_idx += 1
            right_idx -= 1

    return ''.join(list_s)

'''#3：lj's methond ,re'''
import re
def reverseVowels3(s):
    vowel = '[aieouAIEOU]'
    com = re.compile(vowel)
    t = com.findall(s)
    t.reverse()
    k = re.sub(vowel, '✅', s)
    for i in t:
        k = re.sub('✅', i, k, 1)
        # print(k)
    return k


s1 = 'aA'
s2 = 'leetcoad'
print(reverseVowels3(s2))