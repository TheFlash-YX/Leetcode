from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        ans=[]
        s_count=[0]*26
        p_count=[0]*26

        for i in range(len(p)):
            s_count[ord(s[i])-97]+=1
            p_count[ord(p[i])-97]+=1
        if s_count==p_count:
            ans.append(0)

        for i in range(len(s)-len(p)):
            s_count[ord(s[i])-97]-=1
            s_count[ord(s[i+len(p)])-97]+=1
            if s_count==p_count:
                ans.append(i+1)

        return ans


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    solution = Solution()
    ans = solution.findAnagrams(s,p)
    print(ans)