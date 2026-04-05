class Solution:
    # 暴力O(N2)
    def minLength1(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            s=s.replace('AB','').replace('CD','')

        return len(s)

    # 时间复杂度O（N）
    def minLength(self,s:str)->int:
        stack=[]

        for char in s:
            if stack and (char=='B' and stack[-1]=='A' or char=='D' and stack[-1]=='C'):
                stack.pop()
            else:
                stack.append(char)

        return len(stack)



Solution().minLength("D")