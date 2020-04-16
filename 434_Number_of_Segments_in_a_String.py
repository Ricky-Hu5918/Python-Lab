'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
Input: "Hello, my name is John"
Output: 5
'''


class Solution:
    def countSegments1(self, s: str) -> int:
        idx, tmp = 0, ''
        count = 0

        while (idx < len(s)):
            if s[idx] != ' ':
                tmp += s[idx]
            else:
                if (tmp != ''):
                    count += 1
                    tmp = ''

            idx += 1

        return count if not tmp else count + 1

    '''using built-in function'''
    def countSegments2(self, s: str) -> int:
        s = s.split(' ')
        count = 0
        for each in s:
            if each != '':
                count += 1

        return count


    def countSegments3(self, s: str) -> int:
        tmp, ans = '', []

        for each in s:
            if each != ' ':
                tmp += each
            else:
                if tmp != '':
                    ans.append(tmp)
                    tmp = ''

        if tmp != '':
            ans.append(tmp)

        return len(ans)


test = Solution()
s = "  Hello, my name is John  "
print(test.countSegments1(s), test.countSegments2(s), test.countSegments3(s))