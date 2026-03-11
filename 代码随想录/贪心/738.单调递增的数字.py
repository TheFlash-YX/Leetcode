class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        strNum=list(str(n))

        for i in range(len(strNum)-1,0,-1):
            if strNum[i]<strNum[i-1]:
                strNum[i-1]=str(int(strNum[i-1])-1)
                flag=i
                strNum[i:]='9'*(len(strNum)-i)

        num=int(''.join(strNum))

        return num
