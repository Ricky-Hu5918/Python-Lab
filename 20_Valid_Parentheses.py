"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
"""
def isValid(s):
    left_brackets = ['(', '[', '{']
    dic_brackets = {'(': ')', '[': ']', '{': '}'}
    stack_brackets = []

    for i in range(len(s)):
        if (s[i] in left_brackets):
            stack_brackets.append(s[i])
        else:
            if not stack_brackets: return False

            tmp = stack_brackets.pop()
            if (s[i] != dic_brackets[tmp]):
                return False

    return True if not stack_brackets else False

s1 = ')]'
s2 = '('
s3 = '([])'
s4 = '[(})'
print(isValid(s2))