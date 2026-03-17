from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保持 nums1 为短数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            # 边界处理
            max_left1 = nums1[i - 1] if i != 0 else float('-inf')
            min_right1 = nums1[i] if i != m else float('inf')
            max_left2 = nums2[j - 1] if j != 0 else float('-inf')
            min_right2 = nums2[j] if j != n else float('inf')

            # 核心判断逻辑
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # 找到切点，分奇偶讨论
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))
                else:
                    # 修正：使用 / 确保浮点数精度
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0

            elif max_left1 > min_right2:
                # i 太大了，向左收缩
                high = i - 1
            else:
                # i 太小了，向右扩张
                low = i + 1

        # 理论上不会走到这里
        return 0.0
