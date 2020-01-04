'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
"""
#1: 思路：a先把字符串转成int，然后相加得到一个整数；b把整数的数字转成list，然后反转list；'''
        c对list的每一位进行判断，判断时加上一个是否要进位的bool变量，如果最后bool还为真，需要在首位insert一个1
        d将list按位转成十进制整数，最后将整数强转成str返回
"""
def addBinary(a, b):
    target =  int(a) + int(b)

    target_list = []
    while (target != 0):
        target_list.append(target%10)
        target //= 10

    target_list = target_list[::-1]
    bool_addOne = False

    '''#逆序进行for循环'''
    for i in range(len(target_list)-1, -1, -1):
        if ((target_list[i]) == 2):
            if bool_addOne:
                target_list[i] = 1
            else:
                bool_addOne = True
                target_list[i] = 0
        elif (target_list[i] == 1) and bool_addOne:
            target_list[i] = 0
        elif (target_list[i] == 0) and bool_addOne:
            target_list[i] = 1
            bool_addOne = False

    if bool_addOne:
        target_list.insert(0, 1)

    lll = len(target_list) - 1
    rt_int = 0
    for i in range(len(target_list)):
        rt_int += target_list[i]*(10**(lll-i))

    return str(rt_int)

a, b = "11", "1"  #100
a1, b1 = "1010", "1011"  #"10101"
a2, b2 = "1111", "1111"  #"11110"
print(addBinary(a2,b2))