class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre=strs[0]

        for j,c in enumerate(pre):
            for s in strs:
                if j==len(s) or s[j]!=c:
                    return s[:j]
        return pre


