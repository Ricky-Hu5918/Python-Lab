'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 
Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''


class Solution:
    def detectCapitalUse3(self, word: str) -> bool:
        # 3:
        count = 0
        flag = False

        for i in range(len(word)):
            if ord(word[i]) < 97:
                count += 1
                if i == 0: flag = True

        if (count == 0) or (count == len(word)) or (flag and count == 1):
            return True

    # 2:
    def detectCapitalUse2(self, word: str) -> bool:
        if len(word) == 1: return True
        flag = set()

        for i in range(len(word)):
            if word[i].isupper():
                if i!= 0: flag.add(1)
            else:
                flag.add(0)

        return len(flag) == 1

    # 1: normal way
    def detectCapitalUse1(self, word: str) -> bool:
        return word.isupper() or (word[0].isupper() and word[1:].islower()) or word.islower()