# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA,pB=headA,headB

        while pA!=pB:
            pA=pA.next if pA else headB
            pB=pB.next if pB else headA

        return pA


        # 
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        lenA = lenB = 0
        while pA:
            pA = pA.next
            lenA += 1
        while pB:
            pB = pB.next
            lenB += 1

        if lenA < lenB:
            headA, headB = headB, headA

        pA = headA
        pB = headB

        while pB:
            pA = pA.next
            pB = pB.next

        while pA:
            headA = headA.next
            pA = pA.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA


