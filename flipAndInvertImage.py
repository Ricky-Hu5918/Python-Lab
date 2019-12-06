#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 834
def flipAndInvertImage(A):
    for each in A:
        i, j = 0, (len(each) - 1)

        #flip data
        if (len(each) % 2 != 0):
            while (i != j):
                each[i], each[j] = each[j], each[i]
                i += 1
                j -= 1
        else:
            while (i + 1 <= j):
                each[i], each[j] = each[j], each[i]
                i += 1
                j -= 1

        #invert data
        for k in range(len(each)):
            if each[k] == 0:
                each[k] = 1
            else:
                each[k] = 0
    print(A)
    return A


if __name__ == '__main__':
    A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    flipAndInvertImage(A)