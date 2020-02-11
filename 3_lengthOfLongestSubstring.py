"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

'''#1: 92ms'''
def lengthOfLongestSubstring1(s):
    if (not s): return 0
    if (len(s) == 1) or (len(set(s))==1): return 1

    hash_s = {}
    count_list = []

    for i in range(len(s)):
        if (s[i] in hash_s):
            count_list.append(len(hash_s))
            for each in list(hash_s.keys()):
                if each != s[i]:
                    del hash_s[each]
                else:
                    del hash_s[s[i]]
                    break

        hash_s[s[i]] = i

    if not count_list:
        return len(hash_s)
    else:
        return max(max(count_list),len(hash_s))

'''#2: not work, need to be continued'''
def lengthOfLongestSubstring(s):
    if (not s): return 0
    if (len(s) == 1): return 1

    cur_count, max_count = 0, 0
    tmp = ''

    for each in s:
        if (each not in tmp):
            cur_count += 1
            tmp += each
            max_count = cur_count if cur_count >= max_count else max_count
        else:
            print(cur_count, max_count)
            tmp = ''
            tmp += each
            cur_count = 1

    return max_count


s = "dvdf" #3
s1 = "pwwkew"  #3
s2 = "abcabcbb"  #3
s3 = "bbbbb"   #1
s4 = 'bacade'  #4
s5 = 'abcde' #5
s6 = 'abcadef' #6
print(lengthOfLongestSubstring1(s6))