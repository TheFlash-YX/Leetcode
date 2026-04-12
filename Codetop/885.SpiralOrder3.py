class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        dierctions=[(0,1),(1,0),(0,-1),(-1,0)]
        ans=[]
        r=rStart
        c=cStart
        di=0
        step=1

        while len(ans)<rows*cols:
            for _ in range(2):
                for _ in range(step):
                    if 0<=r<rows and 0<=c<cols:
                        ans.append([r,c])
                    r+=dierctions[di][0]
                    c+=dierctions[di][1]
                di=(di+1)%4
            step+=1
        return ans

