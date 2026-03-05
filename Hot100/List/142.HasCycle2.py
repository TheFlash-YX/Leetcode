from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow=fast=head
        len_slow=len_fast=0
        while fast and fast.next:
            if fast==slow:
                break
            slow=slow.next
            fast= fast.next.next
            len_slow+=1
            len_fast+=2

        diff=len_fast-len_slow
        for i in range(diff):
            fast=fast.next

        p=head
        while p!=fast:
            p=p.next
            fast=fast.next

        return p


