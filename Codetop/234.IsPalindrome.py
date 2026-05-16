from typing import Optional
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        head2=self.reverseList(slow)
        while head and head2:
            if head.val!=head2.val:
                return False
            head=head.next
            head2=head2.next

        return True


    def reverseList(self,head):
        pre=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp

        return pre
