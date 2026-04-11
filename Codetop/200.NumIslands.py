class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        ans=0

        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1':
                    self.dfs(grid,r,c,row,col)
                    ans+=1
        return ans

    def dfs(self,grid,r,c,row,col):
        if r<0 or r>=row or c<0 or c>=col or grid[r][c]!='1':
            return


        grid[r][c]='2'

        self.dfs(grid,r-1,c,row,col)
        self.dfs(grid,r+1,c,row,col)
        self.dfs(grid,r,c-1,row,col)
        self.dfs(grid,r,c+1,row,col)



