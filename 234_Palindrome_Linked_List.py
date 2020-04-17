'''
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''


class Solution:
    def isPalindrome2(self, head) -> bool:
        if not head or not head.next: return True

        '''fast and slow pointers'''
        pfast, pslow = head, head
        pre = None
        while (pfast and pfast.next):  # 通过快慢指针，将慢指针指向链表中间
            pslow = pslow.next
            pfast = pfast.next.next

        while (pslow):  # 将后半部分链表切断并翻转，让其指向pre指针
            tmp = pslow.next
            pslow.next = pre
            pre = pslow
            pslow = tmp

        while (head and pre):  # 比较前后两半链表的值，相同则为palindrome
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next

        return True

    '''normal way'''
    def isPalindrome1(self, head) -> bool:
        ans = []
        cur = head
        while cur:
            ans.append(cur.val)
            cur = cur.next

        return ans == ans[::-1]