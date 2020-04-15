'''
Write a program to find the node at which the intersection of two singly linked lists begins.

'''
'''#求的是两个相交链表的起始结点的值'''
'''判断两个链表是否相交，就要看其节点地址是否相等，也就是指向这两个链表中的节点指针是否相等，而不是判断节点的值。'''


class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
    # 2：对齐两个列表的头指针，然后开始遍历并比较两个节点指针，相等则为相交的起点
        lenA, lenB = 0, 0
        pA, pB = headA, headB

        #求出两个链表的长度
        while pA:
            lenA += 1
            pA = pA.next

        while pB:
            lenB += 1
            pB = pB.next

        #重置头指针
        pA, pB = headA, headB

        #让长的链表先走完这个差值
        diff = lenA - lenB
        if (diff>0):
            tmp = diff
            while tmp>0:
                pA = pA.next
                tmp -= 1
        elif (diff < 0):
            tmp = diff
            while tmp<0:
                pB = pB.next
                tmp += 1

        #如果两个链表长度相等，或者长的一方已经走完差值，则继续让它们继续前行，看是否相等
        while (pA != pB):
            pA = pA.next
            pB = pB.next

        return pA

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 1: A走完走B的路，B走完走A的路，相遇则为交点
        # 使两个链表到达相等位置时走过的是相同的距离
        # 链表1的长度是x1+y，链表2的长度是x2+y，我们同时遍历链表1和链表2，到达末尾时，再指向另一个链表。
        # 则当两链表走到相等的位置时：x1+y+x2 = x2+y+x1
        if not headA or not headB: return None

        pA, pB = headA, headB
        while (pA != pB):
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA