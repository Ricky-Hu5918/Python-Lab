'''
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False
'''


class Solution:
    def checkRecord2(self, s: str) -> bool:
        count_A, count_L, idx = 0, 0, 0

        while idx < len(s):
            if s[idx] != 'L':
                count_L = 0
                if s[idx] == 'A': count_A += 1
                if count_A > 1: return False
            else:
                count_L += 1
                if count_L > 2: return False
            idx += 1

        return True

    def checkRecord1(self, s: str) -> bool:
        if "LLL" in s or s.count('A')>1:
            return False
        else:
            return True

    def checkRecord0(self, s: str) -> bool:
        return not (('LLL' in s) or (s.count('A')>1))

    def checkRecord00(self, s: str) -> bool:
        return ('LLL' not in s) and (s.count('A')<=1)

test = Solution()
s = "PPALL"
print(test.checkRecord0(s), test.checkRecord1(s), test.checkRecord2(s), test.checkRecord00(s))