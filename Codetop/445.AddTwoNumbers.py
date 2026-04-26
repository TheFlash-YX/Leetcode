# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        flag = 0
        l1 = self.reverselist(l1)
        l2 = self.reverselist(l2)

        while l1 or l2 or flag > 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            cur_sum = digit1 + digit2 + flag
            flag = cur_sum // 10
            cur_sum = cur_sum % 10

            cur.next = ListNode(val=cur_sum)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return self.reverselist(dummy.next)

    def reverselist(self, l):
        dummy = ListNode()
        pre = None
        while l:
            temp = l.next
            l.next = pre
            pre = l
            l = temp

        return pre


