from linecache import cache


class Solution:
    # 用s和s[::-1]求LCS
    def longestPalindromeSubseq1(self, s: str) -> int:
        ans = self.lcs(s, s[::-1])
        return ans

    def lcs(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i, ch1 in enumerate(text1):
            for j, ch2 in enumerate(text2):
                if ch1 == ch2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[n][m]


    # 递归
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        @cache
        def dfs(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if s[i]==s[j]:
                return dfs(i+1,j-1)+2

            return max(dfs(i+1,j),dfs(i,j-1))

        return dfs(0,n-1)



Solution().longestPalindromeSubseq("bbbab")