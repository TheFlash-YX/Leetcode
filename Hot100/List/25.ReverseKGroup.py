# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p0=dummy=ListNode(0,head)
        cur=head
        length=0

        while cur:
            length+=1
            cur=cur.next

        cur=head
        pre=None

        while length>=k:
            length-=k
            for _ in range(k):
                temp=cur.next
                cur.next=pre
                pre=cur
                cur=temp

            nxt=p0.next
            p0.next.next=cur
            p0.next=pre
            p0=nxt

        return dummy.next