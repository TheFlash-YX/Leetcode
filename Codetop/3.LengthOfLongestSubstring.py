#无重复字符最长子串
class Solution:
    # 两个方法时间复杂度都是O（N）
    # 常规思路，直观好理解
    def lengthOfLongestSubstring1(self, s: str) -> int:
        left=ans=0
        map=set()

        for right,char in enumerate(s):
            while char in map:
                map.remove(s[left])
                left+=1
            map.add(char)
            ans=max(ans,right-left+1)

        return ans


    # 常数级优化，left可以跳跃
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 存放每个字符最后出现的位置
        char_map={}
        left=0
        ans=0

        for right,char in enumerate(s):
            if char in char_map:
                left=max(char_map[char]+1,left)
            char_map[char]=right
            ans=max(ans,right-left+1)


        return ans




