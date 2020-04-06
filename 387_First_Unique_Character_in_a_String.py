'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

import collections
class Find_firstUniqChar:
    def firstUniqChar6(self, s: str) -> int:
    # 6: using built-in method, find() and rfind()
        for each in s:
            if s.find(each) == s.rfind(each):
                return s.index(each)

        return -1

    '''# 5: using hash table'''
    def firstUniqChar5(self, s: str) -> int:
        hash_table = [0 for x in range(26)]

        for each in s:
            hash_table[ord(each) - ord('a')] += 1

        for i in range(len(s)):
            if hash_table[ord(s[i]) - ord('a')] == 1:
                return i

        return -1

    '''# 4: using dictionary'''
    def firstUniqChar4(self, s: str) -> int:
        dict_s = dict()

        for each in s:
            dict_s[each] = dict_s.get(each, 0) + 1

        for k, v in dict_s.items():
            if v == 1:
                return s.index(k)
        return -1

    '''# 3: using count method, not that good'''
    def firstUniqChar3(self, s: str) -> int:
        for each in s:
            if s.count(each) == 1:
                return s.index(each)
        return -1

    '''# 2: traverse method'''
    def firstUniqChar2(self, s: str) -> int:
        if not s: return -1
        checked_chars = ''
        list_s = list(s)
        for i in range(len(s)):
            if list_s[i] not in checked_chars:
                checked_chars += list_s[i]
                if list_s[i] not in list_s[i+1:]:
                    return i

        return -1

    '''# 1: Counter method'''
    def firstUniqChar1(self, s: str) -> int:
        if not s: return -1
        for k, v in collections.Counter(s).items():
            if v == 1:
                return s.index(k)

        return -1

s1, s2 = 'ee', 'loveleetcode'
fc = Find_firstUniqChar()
print(fc.firstUniqChar1(s1), fc.firstUniqChar2(s2))