'''
Implement an algorithm to find the kth to last element of a singly linked list. Return the value of the element.

Note: This problem is slightly different from the original one in the book.

Example:
Input:  1->2->3->4->5 和 k = 2
Output:  4
Note:

k is always valid.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast3(self, head: ListNode, k: int) -> int:
    # 3: 把val取出来放入list中，然后返回list[-k]即可
        if not head: return -1

        ans, cur = [], head
        while (cur):
            ans.append(cur.val)
            cur = cur.next

        return ans[-k]

    '''# 2：先求出链表的长度，倒数第k个节点即为顺数的：总长度 - k + 1 个'''
    def kthToLast2(self, head: ListNode, k: int) -> int:
        if not head: return -1

        len_head, cur = 0, head
        while (cur):
            len_head += 1
            cur = cur.next

        cur = head
        while (len_head - k) > 0:
            cur = cur.next
            k += 1

        return cur.val

    '''# 1: two points'''
    def kthToLast1(self, head: ListNode, k: int) -> int:
        if not head: return -1

        pre, cur = head, head
        for i in range(1, k): #类似于快慢指针，让快指针先移动k-1次
            cur = cur.next

        while (cur.next): #最后同时移动，当快指针到达链表尾部的时候，头指针即为第k个节点
            pre = pre.next
            cur = cur.next

        return pre.val