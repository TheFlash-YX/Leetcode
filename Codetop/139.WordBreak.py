from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        for word in wordDict:
            while word in s:
                s.strip(word)
            if s == "":
                return True

        return False

solution=Solution()
solution.wordBreak("leetcode",["leet","code"])