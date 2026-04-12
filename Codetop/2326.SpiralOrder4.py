# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
        dierctions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di = 0
        matrix = [[-1] * n for _ in range(m)]
        cur = head
        row = col = 0

        while cur:
            matrix[row][col] = cur.val
            cur = cur.next
            x, y = row + dierctions[di][0], col + dierctions[di][1]

            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] != -1:
                di = (di + 1) % 4

            row += dierctions[di][0]
            col += dierctions[di][1]

        return matrix