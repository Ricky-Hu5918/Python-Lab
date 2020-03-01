'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

'''#1: 最后处理第一个元素为val的情况'''
def removeElements1(head, val):
    if not head:
        return head

    pre = head
    cur = head.next
    while cur:
        if cur.val == val:
            pre.next = cur.next
            cur = pre.next
        else:
            pre = pre.next
            cur = cur.next

    return head if head.val != val else head.next

'''#2: 先处理第一个元素为val的情况'''
def removeElements2(head, val):
    if not head:
        return head

    while head and head.val == val:
        head = head.next

    if head:
        pre = head
        cur = head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next

    return head

'''#3: 哨兵节点/伪节点'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def removeElements3(head, val):
    if not head:
        return head

    prepre = ListNode(-1)
    prepre.next = head
    pre = prepre
    cur = head

    while cur:
        if cur.val == val:
            pre.next = cur.next
        else:
            pre = cur

        cur = cur.next

    return prepre.next

'''#4: recursion version'''
def removeElements4(head, val):
    if not head:
        return head

    head.next = removeElements4(head.next, val)

    return head if head.val != val else head.next
