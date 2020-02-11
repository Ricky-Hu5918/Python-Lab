"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
"""

'''#1: recursion version'''
def fib1(n):
    if n==0: return 0
    if n==1: return 1

    if n>1:
        return (fib1(n-1) + fib1(n-2))

'''#2: build a fi sequence'''
def fib2(n):
    fi_seq = []
    fi_seq.append(0)
    fi_seq.append(1)

    for i in range(2, n+2):
        fi_seq.append(fi_seq[i-1]+fi_seq[i-2])

    return fi_seq[n]

'''#3: using while loop to build fn step by step'''
def fib3(n):
    if n<=1: return n

    base0, base1 = 0, 1
    fn_sum, loop_n = 0, 1
    while (loop_n < n):
        loop_n += 1
        fn_sum = base0 + base1
        base0, base1 = base1, fn_sum

    return fn_sum

'''#4: lj's version'''
def fib4(n):
    if n<1: return n

    base0, base1, loop_n = 0, 1, 2
    while (loop_n <= n):
        base0, base1, loop_n = base1, base0+base1, loop_n+1

    return base1

print(fib4(5))
print('fib2', fib2(5))