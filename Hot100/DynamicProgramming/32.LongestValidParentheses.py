class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=[0]*len(s)
        ans=0

        for i in range(1,len(s)):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]=(dp[i-2] if i>=2 else 0 )+2

                elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(':
                    pre_len=dp[i-dp[i-1]-2] if i-dp[i-1]>=2 else 0
                    dp[i]=pre_len+2+dp[i-1]

                ans=max(ans,dp[i])

        return ans
