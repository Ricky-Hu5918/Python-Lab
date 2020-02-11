'''
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

'''#1: normal way, 830ms'''
def isAnagram1(s, t):
    t_list = list(t)

    for each in s:
        try:
            t_list.remove(each)
        except:
            return False

    if not t_list:
        return True
    else:
        return False

'''#2: one-line solution, 36ms'''
from collections import Counter
def isAnagram2(s, t):
    return Counter(s)==Counter(t)

s1, t1 = "anagram", "nagaram"  #true
s2, t2 = 'tarr', 'ratt' #false
s3, t3 = 'a', 'b' #false
print(isAnagram2(s1, t1))
