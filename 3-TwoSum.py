# Brute Force Approach
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# OR

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

# Using Sorting
# Time complexity: O(nlogn)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        thelist = []
        for i,n in enumerate(nums):
            thelist.append([n,i])

        thelist.sort()

        i,j = 0,len(nums)-1

        while(i<j):
            curr = thelist[i][0] + thelist[j][0]
            if curr == target:
                return [min(thelist[i][1],thelist[j][1]),max(thelist[i][1],thelist[j][1])]
            if curr < target:
                i+=1
            else:
                j-=1
        return []

# Using Hash Map
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n]=i
        return []