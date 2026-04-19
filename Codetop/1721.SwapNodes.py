from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p0 = p1 = p2 = dummy = ListNode(next=head)

        for i in range(k):
            p0 = p0.next
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        p0.val, p2.val = p2.val, p0.val

        return dummy.next