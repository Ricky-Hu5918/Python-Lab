#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 557

def reverseWords(s):
    stmp = s.split()
    s2 = []

    for each in stmp:
        s2.append(each[::-1])

    return " ".join(s2)

''' #my solution
    s2 = []
    stmp = ''

    for i in range(len(s)):
        if (s[i] != " "):
            stmp += s[i]
        else:
            stmp = stmp[::-1]
            s2.append(stmp+" ")
            stmp = ''

        if (i+1 == len(s)):
            stmp = stmp[::-1]
            s2.append(stmp)

    s3 = ''
    for each in s2:
        for i in range(len(each)):
            s3 += each[i]
'''

'''
    for each in s2: #反转列表中的字符串
        each = each[::-1]
        print(each)
'''

if __name__ == '__main__':
    s = "Let's take LeetCode contest" #"God Ding"   #"Let's take LeetCode contest"
    ll = reverseWords(s)
    print(ll)