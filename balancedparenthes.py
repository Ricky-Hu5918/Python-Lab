'''
'''
'''
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

Examples:

Input : {[]{()}}
Output : Balanced

Input : [{}{}(]
Output : Unbalanced

[{]}-->Unbalanced
'''
def balanced_parentheses(str):
    p1 = ["{", "}", "[", "]", "(", ")"]

    if (len(str)%2 != 0):
        return "Unbalanced"

    str1 = list(str)
    i, k = 0, 0
    while (len(str1) != 0):
        while (i < len(str1)-1): #找到相邻成对的括号，然后remove掉
            if ((str1[i] == p1[0]) and (str1[i+1] == p1[1])) or ((str1[i] == p1[2]) and (str1[i+1] == p1[3])) or ((str1[i] == p1[4]) and (str1[i+1] == p1[5])):
                str1.pop(i+1)
                str1.pop(i)
                k += 1
                i = 0
            else:
                i += 1

            if (k == 0) and (i == len(str1)-2):
                return "Unbalanced"
        else:
            i, k = 0, 0
    else:
        return "Balanced"

str = "[]({()[{}]})" #"[{]}" #"[(){((()))}()]"  ##"[](){}" #  #"[]({()[{}]})"
print(balanced_parentheses(str))

