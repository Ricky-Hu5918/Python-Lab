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

'''给定了链表和要删除的节点'''
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
