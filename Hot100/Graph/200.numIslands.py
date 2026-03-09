from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.rows=len(grid)
        self.cols=len(grid[0])
        count=0

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c]=='1':
                    count+=1
                    self.dfs(grid, r, c)

        return count

    def dfs(self,grid,r,c)->None:
        if r<0 or c<0 or r>=self.rows or c>=self.cols or grid[r][c]==0:
            return

        grid[r][c] == '0'

        self.dfs(grid,r-1,c)
        self.dfs(grid,r+1,c)
        self.dfs(grid,r,c-1)
        self.dfs(grid,r,c+1)

