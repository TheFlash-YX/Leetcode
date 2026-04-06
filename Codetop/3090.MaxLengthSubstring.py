from collections import defaultdict
from email.policy import default


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_count=defaultdict(int)
        left=ans=0

        for right,char in enumerate(s):
            char_count[char]+=1
            while char_count[char]>2:
                char_count[s[left]]-=1
                left+=1
            ans = max(ans, right - left + 1)
        return ans

Solution().maximumLengthSubstring("bcbbbcba")