class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid]==nums[right]:
                right-=1
            if target == nums[mid]:
                return True

            last_val = nums[right]
            target_left = target > last_val
            mid_left = nums[mid] > last_val

            if target_left == mid_left:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target_left:
                    right = mid - 1
                else:
                    left = mid + 1

        return False

Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2)