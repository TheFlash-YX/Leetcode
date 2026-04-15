from typing import Optional


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        dummy = ListNode(-1)
        cur = dummy

        while l1 or l2 or flag > 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            cur_sum = digit1 + digit2 + flag
            flag = cur_sum // 10
            cur_digit = cur_sum % 10

            node = ListNode(cur_digit)
            cur.next = node
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next






