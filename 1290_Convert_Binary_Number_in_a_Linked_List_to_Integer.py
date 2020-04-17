'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue3(self, head: ListNode) -> int:
        ans = 0
        cur = head

        '''这个比较巧妙，很简洁，效率高'''
        while (cur):
            ans = (ans << 1) + cur.val
            cur = cur.next

        return ans

    '''# 2: same as #3'''
    def getDecimalValue2(self, head: ListNode) -> int:
        ans, res = [], 0
        cur = head

        while (cur):
            ans.append(cur.val)
            cur = cur.next

        ll = len(ans)
        for i in range(ll):
            res += (ans[i] << (ll-1-i))

        return res

    # 1:
    def getDecimalValue1(self, head: ListNode) -> int:
        ans = ''
        cur = head
        while (cur):
            ans += str(cur.val)
            cur = cur.next

        return int('0b'+ans, 2)
