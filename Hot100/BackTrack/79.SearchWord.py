from typing import List


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    if self.backtrack(board,rows,cols,0,r,c,word):
                        return True

        return False

    def backtrack(self,board,rows,cols,index,r,c,word)->bool:
        if index==len(word):
            return True

        if (r<0 or r>=rows) or (c<0 or c>=cols) or (board[r][c]!=word[index]):
            return False
        temp=board[r][c]
        board[r][c]="#"

        found=(
            self.backtrack(board,rows,cols,index+1,r-1,c,word) or
            self.backtrack(board,rows,cols,index+1,r+1,c, word) or
            self.backtrack(board,rows,cols,index+1,r,c-1,word) or
            self.backtrack(board,rows,cols,index+1,r,c+1,word)
        )
        board[r][c]=temp

        return found


if __name__=="__main__":
    board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word="ABCCED"
    solution=Solution()
    ans=solution.exist(board,word)
    print(ans)

