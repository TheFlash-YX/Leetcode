from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s=Counter()
        cnt_t=Counter(t)
        ans_l,ans_r=-1,len(s)
        left=0
        for right,c in enumerate(s):
            cnt_s[c]+=1
            while cnt_s>=cnt_t:
                if right-left<ans_r-ans_l:
                    ans_l,ans_r=left,right
                cnt_s[s[left]]-=1
                left+=1

        return "" if ans_l < 0 else s[ans_l: ans_r + 1]





