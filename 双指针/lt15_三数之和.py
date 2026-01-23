class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if nums[i]>0:
                return result

            if i>0 and nums[i]==nums[i-1]:
                continue

            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    right -= 1
                    left += 1
        return result


if __name__ == '__main__':
    nums=[]
    nums.append(-1)
    nums.append(0)
    nums.append(1)
    nums.append(2)
    nums.append(-1)
    nums.append(-4)

    Solution().threeSum(nums)

