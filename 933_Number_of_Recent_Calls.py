'''
Write a class RecentCounter to count recent requests.
It has only one method: ping(int t), where t represents some time in milliseconds.
Return the number of pings that have been made from 3000 milliseconds ago until now.
Any ping with time in [t - 3000, t] will count, including the current ping.
It is guaranteed that every call to ping uses a strictly larger value of t than before.

Example 1:
Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]

Note:
Each test case will have at most 10000 calls to ping.
Each test case will call ping with strictly increasing values of t.
Each call to ping will have 1 <= t <= 10^9.
'''

'''#1: remove any items which value is less than t-3000.'''
'''标准的队列操作，先进先出，将任一时刻小于t-3000的元素移除,仅保留[t-3000, t]之间的ping操作'''

import collections
class RecentCounter:

    def __init__(self):
        self.q = collections.deque()  #init a deque

    def ping(self, t: int) -> int:
        self.q.append(t) #add an item into the tail of a deque

        while (self.q[0] < (t - 3000)): #check the items from the head of a deque
            self.q.popleft()  #pop items that are less than t-3000

        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

inputs1 = ["RecentCounter","ping","ping","ping","ping"]
q = RecentCounter()
print(q.ping(0))
print(q.ping(1))
print(q.ping(100))
print(q.ping(3001))
print(q.ping(3002))