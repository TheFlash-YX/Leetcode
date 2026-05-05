class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"

        m,n=len(num1),len(num2)
        result=[0]*(m+n)

        for i in range(m-1,-1,-1):
            dig1=int(num1[i])
            for j in range(n-1,-1,-1):
                dig2=int(num2[j])
                mul=dig1*dig2

                pos1=i+j+1
                pos2=i+j
                cur_sum=result[pos1]+mul

                result[pos1]=cur_sum%10
                result[pos2]+=cur_sum//10

        ans="".join(map(str,result))

        return ans if result[0]!=0 else ans[1:]



