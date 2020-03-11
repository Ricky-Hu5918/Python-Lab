'''
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

Example 1:
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"

Example 2:
Input: "               ", 5
Output: "%20%20%20%20%20"
 
Note: 0 <= S.length <= 500000
'''

'''#1: 参考题解'''
def replaceSpaces1(S, length):
    return '%20'.join(S[:length].split(' '))

'''#2: normal method'''
def replaceSpaces2(S, length):
    S_list = list(S)
    res = ''

    for i in range(length):
        if (S_list[i] == ' '):
            S_list[i] = '%20'
        res += S_list[i]

    return res

S1, length1 = "Mr John Smith ", 13
S2, length2 = '               ', 5
print(replaceSpaces2(S2, length2))