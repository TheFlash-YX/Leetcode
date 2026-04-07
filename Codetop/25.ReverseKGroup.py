from stringprep import in_table_c11
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        p0=dummy
        length=0
        cur=head
        while cur:
            length+=1
            cur=cur.next

        pre=None
        cur=head
        while length>k:
            length-=k

            for i in range(k):
                temp=cur.next
                cur.next=pre
                pre=cur
                cur=temp
            nxt=p0.next
            p0.next.next=cur
            p0.next=pre
            p0=nxt

        return dummy.next


head=ListNode(1)
node1=ListNode(2)
node2=ListNode(3)
node3=ListNode(4)
node4=ListNode(5)
head.next=node1
node1.next=node2
node2.next=node3
node3.next=node4
Solution().reverseKGroup(head,2)