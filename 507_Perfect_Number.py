'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''


class Solution:
    def checkPerfectNumber3(self, num: int) -> bool:
        return num in {6, 28, 496, 8128, 33550336}

    # 2: much better
    def checkPerfectNumber2(self, num: int) -> bool:
        if num<6:
            return False

        tmp = num - 1
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                tmp = tmp - i - num//i

        return (tmp == 0)

    # 1: timeout
    def checkPerfectNumber1(self, num: int) -> bool:
        if num<6:
            return False

        ans = [1]
        i = 2
        while i<=num//2:
            if (num%i) == 0:
                ans.append(i)

            i += 1
        return (num == sum(ans))