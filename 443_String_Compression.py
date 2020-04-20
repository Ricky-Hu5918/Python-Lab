'''
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.

Follow up:
Could you solve it using only O(1) extra space?
 
Example 1:
Input:
["a","a","b","b","c","c","c"]
Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 
Example 2:
Input:
["a"]
Output:
Return 1, and the first 1 characters of the input array should be: ["a"]
Explanation:
Nothing is replaced.
 
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
 
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
'''


class Solution:
    def compress3(self, chars) -> int:
        if len(chars) == 1: return 1

        '''主动添加一个字符，能让结尾自然结束而不必单独处理，次字符的选择要避开常规输入，不然会跟输入冲突'''
        chars.append("🐕")

        base = chars[0]
        count, idx = 0, 0
        for each in chars:
            if base == each:
                count += 1
            else:
                chars[idx] = base
                idx += 1
                if (count > 1):
                    for c in (str(count)):
                        chars[idx] = c
                        idx += 1
                count = 1
                base = each

        return idx


    '''解题思路：#2第一个位置存放原始字符，第二个位置存放其数量，超过两位数的数量要分别存放'''
    def compress2(self, chars) -> int:
        if len(chars) == 1: return 1

        base = chars[0]
        count, idx = 0, 0
        for each in chars:
            if base == each:
                count += 1
            else:
                chars[idx] = base
                idx += 1
                if (count > 1):
                    for c in (str(count)):
                        chars[idx] = c
                        idx += 1
                count = 1
                base = each

        chars[idx] = base
        idx += 1
        if (count > 1):
            for c in (str(count)):
                chars[idx] = c
                idx += 1

        return idx

    '''#1: normal way, using extra memory'''
    '''解题思路：利用额外字符串空间存储元素及其出现次数，最后一次复制至原来的字符串中进行覆盖'''
    def compress1(self, chars) -> int:
        if len(chars) == 1: return 1

        ans, count = '', 1
        base = chars[0]
        for each in chars[1:]:
            if base == each:
                count += 1
            else:
                ans += base + (str(count) if count>1 else '')
                count = 1
                base = each

        ans += base + (str(count) if count>1 else '')
        for i in range(len(ans)):
            chars[i] = ans[i]

        return i+1

test = Solution()
#output = ["a","1","3","b","1","9","0","c","1","1"]
chars = ["a","a","a","a","a","a","a","a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c"]
print(test.compress3(chars))
#print(test.compress2(chars))