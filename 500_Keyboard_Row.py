'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''


class Solution:
    def findWords2(self, words):
        # 2: using set() method
        row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        ans = []

        for word in words:
            tmp = set(word.lower())
            if (tmp & row1 == tmp) or (tmp & row2 == tmp) or (tmp & row3 == tmp):
                ans.append(word)

        return ans

    # 1: normal way
    def findWords1(self, words):
        row1, row2, row3 = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        ans = []

        for word in words:
            flag1, flag2, flag3 = False, False, False
            for i in range(len(word)):
                if (word[i].lower() in row1):
                    flag1 = True
                    if flag2 or flag3: break

                if (word[i].lower() in row2):
                    flag2 = True
                    if flag1 or flag3: break

                if (word[i].lower() in row3):
                    flag3 = True
                    if flag1 or flag2: break

                if i == len(word)-1:
                    ans.append(word)

        return ans

    def findWords3(self, words):
        Q = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        A = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        re = []

        for each in words:
            lq = la = lz = 0
            for i in each.lower():
                if (i in Q):
                    lq += 1
                elif (i in A):
                    la += 1
                else:
                    lz += 1

            if (lq == len(each)):
                re.append(each)
            if (la == len(each)):
                re.append(each)
            if (lz == len(each)):
                re.append(each)

        return re

test = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(test.findWords1(words), test.findWords2(words), test.findWords3(words))