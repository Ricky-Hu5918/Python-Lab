'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''

'''#1：二分法'''
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    low, high = 1, n

    while (low < high):
        mid = ((low + high) // 2)
        if (isBadVersion(mid)):
            high = (mid - 1)
            if (isBadVersion(high) == False):
                return mid
        else:
            low = (mid + 1)
            if (isBadVersion(low) == True):
                return low

'''#2：二分法，a better version, only calling API once'''
def firstBadVersion2(self, n):
    """
    :type n: int
    :rtype: int
    """
    low, high = 1, n

    while (low < high):
        mid = ((low + high) // 2)
        if (isBadVersion(mid)):
            high = (mid)
        else:
            low = (mid + 1)

    return low

'''#3: recursion version from xk, but timeout, maximum recursion depth'''
def firstBadVersion3(self, n):
    """
    :type n: int
    :rtype: int
    """
    return check_recursive(1, n)

def check_recursive(start, end):
    if start == end:
        return start

    if isBadVersion(start):
        return start
    else:
        return check_recursive(start+1, end)
