'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''#1：single point'''
def middleNode1(head):
    count, ans = 0, ListNode(-1)
    cur = head

    while (cur != None):  #find the length of the listnode
        count += 1
        cur = cur.next

    idx = (count//2) + 1  #find the index of the middle node
    count = 0
    while (head != None):
        count += 1
        if (count == idx):
            ans.val = head.val
            ans.next = head.next
            break
        head = head.next

    return ans

'''#2: I can't understand this solution'''
def middleNode2(head):
    ans = [head]

    while (ans[-1].next):
        ans.append(ans[-1].next)

    return ans[len(ans)//2]

'''#3: two point, fast and slow point'''
def middleNode3(head):
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

