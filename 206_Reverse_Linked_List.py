'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList2(self, head: ListNode) -> ListNode:
        # 2: recursion
        if not head or not head.next: return head

        node = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return node

    '''1: iterate'''
    def reverseList1(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        pre = head
        new_head = None
        while (pre):
            tmp = pre.next
            pre.next = new_head
            new_head = pre
            pre = tmp

        return new_head
