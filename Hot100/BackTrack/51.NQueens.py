
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res=[]
        self.queens=[-1]*n
        self.cols=set()
        self.diag1=set()
        self.diag2=set()

        self.backtrack(0,n)

        return self.res


    def backtrack(self,row,n):
        if row==n:
            board=["."*c+"Q"+"."*(n-c-1) for c in self.queens]
            self.res.append(board)
            return self.res

        for col in range(n):
            d1=row-col
            d2=row+col

            if col in self.cols or d1 in self.diag1 or d2 in self.diag2:
                continue

            self.queens[row]=col
            self.cols.add(col)
            self.diag1.add(d1)
            self.diag2.add(d2)

            self.backtrack(row+1,n)

            self.cols.remove(col)
            self.diag1.remove(d1)
            self.diag2.remove(d2)


