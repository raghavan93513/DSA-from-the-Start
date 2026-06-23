# Two Sum II - Input Array Is Sorted
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            if numbers[l]+numbers[r]>target:
                r-=1
            else:
                l+=1
        return []

# Hash Map Approach
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in hashmap:
                return [hashmap[diff]+1,i+1]
            hashmap[n]=i
        return []