class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.result=[]
        self.backtrack(n,k,[],1)
        return self.result



    def backtrack(self,n,k,path,index):
        if len(path)==k:
            self.result.append(path[:])
            return
        need=k-len(path)

        for i in range(index,n-need+2):
            path.append(i)
            self.backtrack(n,k,path,i+1)
            path.pop()