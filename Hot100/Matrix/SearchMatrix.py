
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        row,col=0,0
        left,right=0,m*n-1
        while left<=right:
            mid=(left+right)//2
            row=mid//n
            col=mid%n
            mid_val=matrix[row][col]
            if mid_val>target:
                right=mid-1
            elif mid_val<target:
                left=mid+1
            else:
                return True

        return False

solution=Solution()
mat=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
ans=solution.searchMatrix(mat,3)
print(ans)