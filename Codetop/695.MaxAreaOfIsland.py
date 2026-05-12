class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        area=0

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    cur_area=self.dfs(grid,r,c,row,col)
                    area=max(area,cur_area)

        return area

    def dfs(self,grid,r,c,row,col):
        if r<0 or r>=row or c<0 or c>=col or grid[r][c]==0:
            return 0
        grid[r][c]==0
        area=1
        area+=self.dfs(grid,r-1,c,row,col)
        area+=self.dfs(grid,r+1,c,row,col)
        area+=self.dfs(grid,r,c-1,row,col)
        area+=self.dfs(grid,r,c+1,row,col)

        return area