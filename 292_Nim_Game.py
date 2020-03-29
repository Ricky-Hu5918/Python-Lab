'''
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be
             removed by your friend.
'''

'''#思路：如果n能被4整除，则无论如何我们第一次拿多少，最后都会被对手拿走剩下的，也就是我们会输；\
如果n不能被4整除，则最后我们都会把4留给对手，也就是我们会赢'''

def canWinNim1(n):
    return True if n%4 else False

def canWinNim2(n):
    return (n%4)