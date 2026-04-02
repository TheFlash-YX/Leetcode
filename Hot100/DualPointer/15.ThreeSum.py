class Solution:
    def threeSum1(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]

        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue

            left=i+1
            right=len(nums)-1

            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1

                    left+=1
                    right-=1

        return ans


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]

        for i in range(len(nums)-2):
            x=nums[i]
            if i>0 and x==nums[i-1]:
                continue
            if x+nums[i+1]+nums[i+2]>0:
                break
            if x+nums[-2]+nums[-1]<0:
                continue

            ans.append((x,nums[i+1],nums[i+2]))

        return ans

Solution().threeSum([-1,0,1,2,-1,-4])