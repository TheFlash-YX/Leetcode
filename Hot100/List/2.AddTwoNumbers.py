from string import Template
from sys import flags
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        cur=dummy
        flag=0

        while l1 or l2 or flag:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            temp=val1+val2+flag
            flag=temp//10

            cur.next=ListNode(temp%10)
            cur=cur.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return dummy.next