# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        pre=dummy

        while pre.next and pre.next.next:
            node1=pre.next
            node2=pre.next.next

            node1.next =node2.next
            node2.next=node1
            pre.next=node2

            pre=node1

        return dummy.next


