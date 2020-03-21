'''
Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

Example1:
Input: "tactcoa"
Output: true（permutations: "tacocat"、"atcocta", etc.）
'''
'''#1: normal way'''
from collections import Counter
def canPermutePalindrome(s):
    if not s: return True
    count_odd, count_even = 0, 0

    for v in Counter(s).values():
        if v%2:
            count_odd += 1
        else:
            count_even += 1

    if count_odd == 1:
        return True
    elif (not count_odd) and (count_even):
        return True
    else:
        return False

s1 = 'abcab'
s2 = 'aabb'
s3 = 'a'
print(canPermutePalindrome(s2))