from typing import Optional
class ListNode:
    def __init__(self,val=0,next=None):
        self.next=next
        self.val=val

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        pre=None
        cur=dummy.next

        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp

        return pre

    def reverseList(self,head:Optional[ListNode])->Optional[ListNode]:
        if not head or not head.next:
            return head

        rev_head=self.reverseList(head.next)
        tail=head.next
        tail.next=head
        head.next=None

        return rev_head

