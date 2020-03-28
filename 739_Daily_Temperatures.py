'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note:
The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
'''

'''#1: stack version'''
'''注意：stack中的元素是T中元素的下标，即index'''
def dailyTemperatures1(T):
    stack = []
    res = [0 for x in range(len(T))]

    for i in range(len(T)):
        while (stack) and (T[i] > T[stack[-1]]): #循环比较即将入栈的元素与栈顶元素的大小
            pre_idx = stack.pop()  #满足温升条件，弹出前一个元素的下标
            res[pre_idx] = i - pre_idx  #当前下标与前一个元素下标的差值即为等待温升的天数

        stack.append(i)  #入栈前一个元素的下标

    return res


'''#2: normal way, timeout'''
def dailyTemperatures2(T):
    days = []

    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            if T[i] < T[j]:
                days.append(j - i)
                break

            if (j == len(T) - 1):
                days.append(0)

    days.append(0)
    return days


T1 = [73,74,75,71,69,72,76,73]   #[1, 1, 4, 2, 1, 1, 0, 0]
T2 = [89,62,70,58,47,47,46,76,100,70]   #[8,1,5,4,3,2,1,1,0,0]
print(dailyTemperatures1(T2))
print(dailyTemperatures2(T2))