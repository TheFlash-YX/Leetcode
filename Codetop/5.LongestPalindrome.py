class Solution:
    # 把奇偶字符串分开处理
    def longestPalindrome1(self, s: str) -> str:
        n=len(s)
        ans_left=ans_right=0
        # 奇数

        for i in range(n):
            l=r=i
            while l>=0 and r<=n-1 and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1 > ans_right-ans_left:
                ans_left=l+1
                ans_right=r


        for i in range(n-1):
            l=i
            r=i+1
            while l>=0 and r<=n-1 and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1>ans_right-ans_left:
                ans_left=l+1
                ans_right=r

        return s[ans_left:ans_right]

    # 把奇偶情况合并
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans_left=ans_right=0

        for i in range(2*n-1):
            l=i//2
            r=(i+1)//2

            while l>=0 and r<=n-1 and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1 > ans_right-ans_left:
                ans_left=l+1
                ans_right=r

        return s[ans_left:ans_right]












