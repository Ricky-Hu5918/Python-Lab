'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def deleteDuplicates(head):
    pre = head
    cur = head.next

    while (cur != None):
        if (pre.value == cur.value):
            pre.next = cur.next
            cur = pre.next
        else:
            pre = cur
            cur = cur.next

    return head

head = [1,2,2,3,4,4]
print(deleteDuplicates(head))
