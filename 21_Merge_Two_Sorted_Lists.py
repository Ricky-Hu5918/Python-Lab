'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if not l1 and l2:
        return l2
    elif not l2 and l1:
        return l1
    else:
        return l1

    cur1, cur2 = l1, l2
    if cur1.val < cur2.val:
        mergedlists = ListNode(cur1.val)
        cur1 = cur1.next
    else:
        mergedlists = ListNode(cur2.val)
        cur2 = cur2.next

    cur3 = mergedlists
    while (cur1 or cur2):
        if not cur1 and cur2:
            cur3.next = ListNode(cur2.val)
            cur2 = cur2.next
        elif not cur2 and cur1:
            cur3.next = ListNode(cur1.val)
            cur1 = cur1.next
        else:
            if cur1.val < cur2.val:
                cur3.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                cur3.next = ListNode(cur2.val)
                cur2 = cur2.next

        cur3 = cur3.next

    return mergedlists


'''#2: 迭代版本'''
def mergeTwoLists2(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    else:
        if l1.val < l2.val:
            l1.next = mergeTwoLists2(l1.next, l2) #self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists2(l2.next, l2) #self.mergeTwoLists2(l2.next, l2)
            return l2

'''#3: 递归版本'''
def mergeTwoLists3(l1, l2):
    prehead = ListNode(-1)
    pre = prehead

    while (l1 and l2):
        if l1.val < l2.val:
            pre.next = l1
            l1 = l1.next
        else:
            pre.next = l2
            l2 = l2.next

        pre = pre.next

    pre.next = l1 if l1 is not None else l2

    return prehead.next





