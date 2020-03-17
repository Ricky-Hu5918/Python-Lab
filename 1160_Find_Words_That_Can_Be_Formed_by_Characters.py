'''
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
'''

'''#1: normal solution'''
from collections import Counter
def countCharacters(words, chars):
    count, res = 0, 0
    chars_dict = Counter(chars)

    for each in words:
        each_dict = Counter(each)
        for i in range(len(each)):
            if each_dict[each[i]] > chars_dict.get(each[i], 0):
                count = 0
                break
            else:
                count += 1

        res += count
        count = 0

    return res

words, chars = ["hello","world","leetcode"], "welldonehoneyr"
print(countCharacters(words, chars)) #10