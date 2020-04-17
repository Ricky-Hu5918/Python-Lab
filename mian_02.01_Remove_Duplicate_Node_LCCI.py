'''
Write code to remove duplicates from an unsorted linked list.

Example1:
Input: [1, 2, 3, 3, 2, 1]
Output: [1, 2, 3]

Example2:
Input: [1, 1, 1, 1, 2]
Output: [1, 2]

Note:
The length of the list is within the range[0, 20000].
The values of the list elements are within the range [0, 20000].

Follow Up:
How would you solve this problem if a temporary buffer is not allowed?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''#3: timeout, same as #2, not using extra buffer'''
    def removeDuplicateNodes3(self, head: ListNode) -> ListNode:
        if not head: return head

        cur = head
        while (cur):
            second = cur
            while (second.next):
                if (cur.val == second.next.val):
                    second.next = second.next.next
                else:
                    second = second.next

            cur = cur.next

        return head

    '''#2: timeout, not using extra buffer'''
    def removeDuplicateNodes2(self, head: ListNode) -> ListNode:
        if not head: return head

        start = head
        while start:
            pre = start
            cur = start.next
            while cur:
                if start.val == cur.val:
                    pre.next = cur.next
                else:
                    pre = cur

                cur = cur.next

            start = start.next

        return head

    '''# 1: normal way, 使用list，效率是秒级，而使用set，其效率是100ms级，差距非常大，以后尽量都用set'''
    def removeDuplicateNodes1(self, head: ListNode) -> ListNode:
        if not head: return head

        #ans = []
        ans = set()
        ans.add(head.val)
        pre = head
        cur = head.next

        while (cur):
            if (cur.val not in ans):
                ans.add(cur.val)
                pre = cur
            else:
                pre.next = cur.next

            cur = cur.next

        return head