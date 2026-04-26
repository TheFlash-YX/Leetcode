class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        pos1 = pos2 = -1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pos1 = i
                break

        if pos1 >= 0:
            for i in range(len(nums) - 1, -1, -1):
                if nums[pos1] < nums[i]:
                    pos2 = i
                    break
            # 或者用双指针来交换数值，空间复杂度O(1)
            nums[pos1], nums[pos2] = nums[pos2], nums[pos1]
            nums[pos1 + 1:] = nums[pos1 + 1:][::-1]
        else:
            nums.reverse()


Solution().nextPermutation([1,3,2])