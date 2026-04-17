class Solution:
    def trap(self, height: list[int]) -> int:
        ans = left = 0
        right = len(height) - 1
        pre_max = height[0]
        suf_max = height[-1]

        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max > suf_max:
                ans += suf_max - height[right]
                right -= 1
            else:
                ans += pre_max - height[left]
                left += 1

        return ans


