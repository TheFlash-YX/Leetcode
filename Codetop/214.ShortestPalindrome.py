class Solution:
    def shortestPalindrome(self, s: str) -> str:


    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_left = ans_right = 0

        for i in range(2 * n - 1):
            l = i // 2
            r = (i + 1) // 2
            while l >= 0 and r <= n - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans_right - ans_left:
                ans_left = l + 1
                ans_right = r

        return 