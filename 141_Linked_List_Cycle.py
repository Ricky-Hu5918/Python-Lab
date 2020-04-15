'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle3(self, head: ListNode) -> bool:
    # 3： hash策略
        if not head: return False

        #遍历过程中将val置为None
        while (head.next and head.val != None):
            head.val = None
            head = head.next

        #如果是因为next指针为None而退出循环，则无环
        if not head.next: return False

        #如果是因为val为None而退出循环，则有环
        return True

    def hasCycle2(self, head: ListNode) -> bool:
    # 2：fast and slow pointers
        if not head or not head.next: return False
        pslow = head
        pfast = head.next

        while (pslow != pfast):
            if not pfast.next or not pfast.next.next:
                return False

            pslow = pslow.next
            pfast = pfast.next.next

        return True

    def hasCycle1(self, head: ListNode) -> bool:
    # 1：fast and slow pointers
        if not head: return False

        pslow, pfast = head, head #同时起跑
        while True:
            if (not pfast.next) or (not pfast.next.next): #排除pfast.next及pfast.next.next为空的情况
                return False

            pslow = pslow.next
            pfast = pfast.next.next

            if (pfast == pslow) or (pfast.next == pslow): #快指针追上了慢指针，或超过了慢指针
                return True