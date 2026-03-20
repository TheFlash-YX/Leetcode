#无重复字符最长子串
class Solution:
    #常规思路，直观好理解
    def lengthOfLongestSubstring1(self, s: str) -> int:
        left = 0
        ans = 0
        occ = set()

        for right, char in enumerate(s):
            while char in occ:
                occ.remove(s[left])
                left += 1
            occ.add(char)
            right += 1
            ans = max(ans, right - left)
        return ans


    # 优化，left可以跳跃
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 存放每个字符最后出现的位置
        char_map={}
        left=0
        ans=0

        for right in range(len(s)):
            cur_char=s[right]
            if cur_char in char_map:
                # 防止字符上一次出现的位置在原本的left之后
                # left不能回退
                left=max(left,char_map[cur_char]+1)
            char_map[cur_char]=right
            ans=max(ans,right-left+1)

        return ans




