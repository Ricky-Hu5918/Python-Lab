'''
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：
输入: n = 5, m = 3
输出: 3

示例 2：
输入: n = 10, m = 17
输出: 2
 
限制：
1 <= n <= 10^5
1 <= m <= 10^6
'''

'''#1: 暴力破解法'''
def lastRemaining1(n, m):
    ans = [x for x in range(n)]
    idx = 0

    while (len(ans) != 1):
        idx = (idx + m - 1) % (len(ans))
        ans.pop(idx)

    return ans[0]

'''#2: 数学方法，但是没有理解'''
def lastRemaining2(n, m):
    res = 0

    '''#最后一轮剩下2个人，所以从2开始反推'''
    for i in range(2, n+1):
        res = (res + m) % i

    return res

n1, m1 = 5, 3  #3
n2, m2 = 10, 17  #2
print(lastRemaining2(n1, m1))