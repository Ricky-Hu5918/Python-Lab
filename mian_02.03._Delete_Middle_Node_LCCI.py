'''
同第237题

Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

Example:
Input: the node c from the linked list a->b->c->d->e->f
Output: nothing is returned, but the new linked list looks like a->b->d->e->f
'''
'''题目的意思是：将给出的节点node删除'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''给定了node节点，将其在链表中删除。方法：修改node的val为下一个节点，然后将下一个节点删除'''
class Solution1:
    def deleteNode1(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

'''给定了链表和要删除的节点，要删除的节点不包含头节点和尾节点'''
class Solution2:
    def deleteNode2(self, node: ListNode, n: int) -> None:
        """
        Do not return anything, modify node in-place instead.
        """

        #遍历，寻找该节点，然后将next节点的值赋值给该节点，最后删除next节点
        cur = node
        while True:
            if cur.val == n:
                cur.val = cur.next.val
                cur.next = cur.next.next
                break
            else:
                cur = cur.next

'''#面试题18. 删除链表的节点(节点包含头、尾节点)
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
'''

class DeleteNode:
    def deleteNode1(self, head: ListNode, val: int) -> ListNode:
        if not head: return head

        H = ListNode(-1) #伪头结点
        H.next = head
        pre, cur = H, H.next
        while cur:
            if (cur.val == val):
                pre.next = cur.next  #直接删
            cur = cur.next
            pre = pre.next

        return H.next

    #1:
    def deleteNode2(self, head: ListNode, val: int) -> ListNode:
        if not head: return head

        H = ListNode(-1) #伪头结点
        H.next = head
        pre, cur = H, H.next
        while cur.next:
            if (cur.val == val):
                cur.val = cur.next.val   #用后一个结点的值覆盖当前节点，再删除后一个结点
                cur.next = cur.next.next
            else:
                cur = cur.next
            pre = pre.next

        if cur.val == val and not cur.next: #处理最后一个节点
            pre.next = None

        return H.next

    '''A better way'''
    def deleteNode3(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        if head.val == val: return head.next

        pre, cur = head, head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next

            cur = cur.next
            pre = pre.next

        return head
