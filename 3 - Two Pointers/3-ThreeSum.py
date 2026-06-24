# Three Sum - Fix the target as the negative of first number. Then it is just a 2 sum problem
# Time complexity: O(n^2)
# Space complexity: O(1)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            j,k = i+1,len(nums)-1
            while j<k:
                if nums[j]+nums[k]==target:
                    result.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]: #Skip the duplicates
                        j+=1
                    while k>j and nums[k]==nums[k-1]: #Skip the duplicates
                        k-=1
                    j+=1
                    k-=1
                elif nums[j]+nums[k]<target:
                    j+=1
                else:
                    k-=1
        return result