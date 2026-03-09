from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.rows=len(grid)
        self.cols=len(grid[0])
        fresh_count=0
        queue=deque()
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c]==1:
                    fresh_count+=1
                elif grid[r][c]==2:
                    queue.append((r,c))

        if fresh_count==0:
            return 0
        return self.bfs(grid,queue,fresh_count)

    def bfs(self,grid,queue,fresh_count)->int:

        minutes=0
        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        while queue and fresh_count>0:
            minutes += 1
            level_size = len(queue)
            for _ in range(level_size):
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<self.rows and 0<=nc<self.cols and grid[nr][nc]==1:

                        grid[nr][nc]=2
                        fresh_count-=1
                        queue.append((nr,nc))

        return minutes if fresh_count==0 else -1






