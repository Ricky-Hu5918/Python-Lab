'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
 

Note:

1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
'''
import collections
class Solution:
    def mostCommonWord2(self, paragraph: str, banned) -> str:
        '''replace non-string with space'''
        for ch in paragraph:
            if ch in (' ', '!', '?', '.', ';', ',', "'"):
                paragraph = paragraph.replace(ch, ' ')
        paragraph = paragraph.lower() #change all string to lower characters
        '''#split the string with space'''
        para_list = paragraph.split()  #此处使用.split(' ')会有问题，why？

        tmp = collections.Counter(para_list)
        max_times, res_word = 0, ''
        for k, v in tmp.items():
            if (k not in set(banned)) and (v > max_times):
                max_times = v
                res_word = k

        return res_word

    '''#1: '''
    def mostCommonWord1(self, paragraph: str, banned) -> str:
        res, tmp_s = [], ''
        for each in paragraph:
            if each not in (' ', '!', '?', '.', ';', ',', "'"):
                tmp_s += each.lower()
            else:
                if tmp_s:
                    res.append(tmp_s)
                    tmp_s = ''

        if tmp_s: res.append(tmp_s)

        tmp = collections.Counter(res)
        for item in banned:
            del tmp[item]

        for k, v in tmp.items():
            if v == (max(tmp.values())):
                return k

test = Solution()
paragraph, banned = "Bob hit a ball, the hit BALL flew far after it was hit.", ["bob", "hit"]
print(test.mostCommonWord1(paragraph, banned), test.mostCommonWord2(paragraph, banned))