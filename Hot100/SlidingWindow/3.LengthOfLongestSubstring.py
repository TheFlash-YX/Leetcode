class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ=set()
        left=0
        right=-1
        ans=0

        for left in range(len(s)):
            if left !=0:
                occ.remove(s[left-1])
            while right+1<len(s) and s[right+1] not in occ:
                occ.add(s[right+1])
                right+=1
            ans=max(ans,right-left+1)

        return ans




if __name__=="__main__":
    s="abcabcbb"
    solution=Solution()
    ans=solution.lengthOfLongestSubstring(s)
    print(ans)