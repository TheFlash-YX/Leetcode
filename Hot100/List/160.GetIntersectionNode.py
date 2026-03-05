#Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA,pB=headA,headB
        while pA!=pB:
            if pA:
                pA=pA.next
            else:
                pA=headB
            if pB:
                pB=pB.next
            else:
                pB=headA

        return pA


def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    def get_length(node:ListNode)->int:
        length=0
        while node:
            node=node.next
            length+=1
        return length

    lenA=get_length(headA)
    lenB=get_length(headB)
    pA, pB =headA,headB

    if lenA<lenB:
        pA,pB=pB,pA
        lenA,lenB=lenB,lenA

    diff=lenA-lenB
    for i in range(diff):
        pA=pA.next

    while pA!=pB:
        pA = pA.next
        pB = pB.next

    return pA