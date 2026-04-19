from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        cur=dummy.next

        while cur and cur.next:
            while cur.val==cur.next.val and cur.next:
                cur.next=cur.next.next
            cur=cur.next
        return dummy.next


