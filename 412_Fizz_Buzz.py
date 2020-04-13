'''
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


class Solution:
    def fizzBuzz1(self, n: int):
        dict_ans = dict()

        for i in range(1, n + 1):
            if (i % 3 == 0) and (i % 5):
                dict_ans[i] = "Fizz"
            elif (i % 3) and (i % 5 == 0):
                dict_ans[i] = "Buzz"
            elif (not i % 3) and (not i % 5):
                dict_ans[i] = "FizzBuzz"
            else:
                dict_ans[i] = str(i)

        return list(dict_ans.values())

    '''2: '''
    def fizzBuzz2(self, n: int):
        ans, idx = [], 1

        while (idx <= n):
            if (idx%3 == 0) and (idx%5):
                ans.append("Fizz")
            elif (idx%3) and (idx%5 == 0):
                ans.append("Buzz")
            elif (idx%3 == 0) and (idx%5 == 0):
                ans.append("FizzBuzz")
            else:
                ans.append(str(idx))

            idx += 1

        return ans

    '''#3: '''
    def fizzBuzz3(self, n: int):
        ans = [str(x) for x in range(1, n+1)]

        for k, v in enumerate(ans):
            if (int(v) % 3 == 0) and (int(v) % 5):
                ans[k] = "Fizz"
            elif (int(v) % 5 == 0) and (int(v) % 3):
                ans[k] = "Buzz"
            elif (int(v) % 3 == 0) and (int(v) % 5 == 0):
                ans[k] = "FizzBuzz"

        return ans

fb = Solution()
print(fb.fizzBuzz1(20), '\n', fb.fizzBuzz2(20), '\n', fb.fizzBuzz3(20))