class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        i=0


        while i<n and s[i]==" ":
            i+=1

        sign = 1
        if i<n and s[i] in "-+":
            sign=1 if s[i]=="+" else -1
            i+=1

        MX=(1<<31) -1
        num=0

        while i<n and '0'<=s[i]<='9':
            num=num*10+int(s[i])
            if num>MX:
                return MX if sign>0 else -(1<<31)
            i+=1

        return sign*num








