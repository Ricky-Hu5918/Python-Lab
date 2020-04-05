'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
import collections

class Solution:
    def canConstruct6(self, ransomNote: str, magazine: str) -> bool:
        return (collections.Counter(ransomNote) & collections.Counter(magazine)) == collections.Counter(ransomNote)

    '''#5: hash table'''
    def canConstruct5(self, ransomNote: str, magazine: str) -> bool:
        hash_table = [0 for x in range(26)]

        for each in magazine:
            hash_table[ord(each) - ord('a')] += 1

        for each in ransomNote:
            hash_table[ord(each) - ord('a')] -= 1
            if (hash_table[ord(each) - ord('a')] < 0):
                return False

        return True

    '''# 4: a better version same as #3'''
    def canConstruct4(self, ransomNote: str, magazine: str) -> bool:
        list_magazine = list(magazine)

        for each in ransomNote:
            try:
                list_magazine.remove(each)
            except:
                return False

        return True

    '''# 3: using list method'''
    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        list_ransom = list(ransomNote)
        list_magazine = list(magazine)

        for each in list_ransom:
            if each in list_magazine:
                list_magazine.remove(each)
            else:
                return False

        return True

    '''# 2: using Counter method'''
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        for k, v in collections.Counter(ransomNote).items():
            if k not in collections.Counter(magazine).keys():
                return False
            elif collections.Counter(magazine)[k] < v:
                return False

        return True

    '''# 1: using built-in method count'''
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        for each in ransomNote:
            if each not in magazine:
                return False
            elif (ransomNote.count(each) > magazine.count(each)):
                return False

        return True

ransomNote = 'aab'
magazine = 'abb'
q = Solution()
print(q.canConstruct6(ransomNote,magazine))