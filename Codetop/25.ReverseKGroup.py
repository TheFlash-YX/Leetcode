from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        pre=dummy


        while True:
            tail = pre
            for _ in range(k):
                tail=tail.next
                if not tail:
                    return dummy.next

            nex=tail.next

            tail.next=None
            head_cur=pre.next

            self.reverseList(head_cur)

            head_cur.next=nex
            pre.next=tail

            pre=head_cur



    def reverseList(self,head):
        pre=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp

        return pre
