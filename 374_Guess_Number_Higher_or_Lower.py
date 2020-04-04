'''
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example :
Input: n = 10, pick = 6
Output: 6
'''

class Solution:
    '''#1: binary research'''
    def guessNumber1(self, n: int) -> int:
        low, high = 1, n

        while (low <= high):
            mid = low + (high-low)//2
            guess_result = guess(mid)
            if (guess_result == 0):
                return mid
            elif (guess_result == 1):
                low = mid + 1
            else:
                high = mid - 1

        return -1

    '''#2: recursion version'''
    def guessNumber2(self, n: int) -> int:
        if (guess(n) == 0):
            return n
        else:
            n -= 1
            return self.guessNumber2(n)

    '''#3: traverse version'''
    def guessNumber3(self, n: int) -> int:
        for i in range(1, n+1):
            if (guess(i) == 0):
                return i

        return -1
