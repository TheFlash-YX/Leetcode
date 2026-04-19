from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = p2 = dummy = ListNode(next=head)

        for i in range(n):
            p1 = p1.next

        while p1.next:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return dummy.next