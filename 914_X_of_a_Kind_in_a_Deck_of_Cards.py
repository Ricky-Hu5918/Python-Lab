'''
In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
Each group has exactly X cards.
All the cards in each group have the same integer.

Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:
Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.

Example 3:
Input: deck = [1]
Output: false
Explanation: No possible partition.

Example 4:
Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].

Example 5:
Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].

Constraints:
1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
'''

'''#1: 统计card的出现次数，求所有出现次数的最大公约数，大于1则返回True'''
from functools import reduce
from collections import Counter
from math import gcd
def hasGroupsSizeX1(deck) -> bool:
    return reduce(gcd, Counter(deck).values()) >= 2


'''#2: 不用系统自带的库，自己写求最大公约数的函数，自己写统计出现次数的函数'''
def hasGroupsSizeX2(deck) -> bool:
    dict_deck = dict()
    for each in deck:  #统计次数
        dict_deck[each] = dict_deck.get(each, 0) + 1

    #求最大公约数
    x = -1
    for each in dict_deck.values():
        x = each if x == -1 else mygcd(x, each)
        if x == 1:
            return False

    return x >= 2

def mygcd(a, b):
    return a if b==0 else mygcd(b, a%b)


deck1 = [1,1,1,1,2,2,2,2,2,2,3,3] #true
deck2 = [1,2,3,4] #false
print(hasGroupsSizeX2(deck2))