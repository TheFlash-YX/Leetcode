class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i, char1 in enumerate(text1):
            for j, char2 in enumerate(text2):
                if char1 == char2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[m][n]

Solution().longestCommonSubsequence("bbbab","babbb")