'''
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number
by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
'''#1: not very good'''
def isHappy1(n):
    tmp = []
    while (n != 1):
        n = split_and_square(n)
        if (n not in tmp):
            tmp.append(n)
        else:
            return False

    return True

def split_and_square(n):
    new_n = 0
    while (n>0):
        new_n += (n%10)*(n%10)
        n //= 10

    return new_n

'''#2: same as #1'''
def isHappy2(n):
    tmp = []
    while (n != 1):
        new_n = 0
        while (n > 0):
            new_n += (n % 10) * (n % 10)
            n //= 10
        n = new_n
        if (n not in tmp):
            tmp.append(n)
        else:
            return False
    return True

'''#3: recursion version, using a global list'''
tmp = []
def isHappy3(n):
    if n==1: return True
    print(tmp)
    if n not in tmp:
        tmp.append(n)
    else:
        return False

    new_n = 0
    while (n>0):
        new_n += (n%10)*(n%10)
        n //= 10
    #print(new_n)
    return isHappy3(new_n)

'''#4: recursion version 2. not happy number must become 4 during the process'''
def isHappy4(n):
    if (n==1): return True
    if (n==4): return False

    new_n = 0
    while (n>0):
        k = (n%10)
        new_n += (k*k)
        n //= 10

    return isHappy4(new_n)

n = 1119
print(isHappy4(n))