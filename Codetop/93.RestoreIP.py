class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        self.result=[]
        self.backtrack(s,[],0)
        return self.result


    def backtrack(self,s,path,index):
        if len(path)==4 and index==len(s):
            self.result.append(".".join(path[:]))
            return

        for i in range(index,min(index+3,len(s))):
            seg=s[index:i+1]

            if len(seg)>1 and seg[0]=='0':
                break

            if 0<=int(seg)<=255:
                path.append(seg)
                self.backtrack(s,path,i+1)
                path.pop()