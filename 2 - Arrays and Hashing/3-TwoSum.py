# Using Sorting
# Time complexity: O(nlogn)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i,n in enumerate(nums):
            arr.append([n,i])

        arr.sort()
        i,j = 0,len(nums)-1

        while(i<j):
            curr = arr[i][0]+arr[j][0]
            if curr==target:
                return [arr[i][1],arr[j][1]]
            elif curr<target:
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

# Revised on 8th June 2026
# Revised on 24th September 2026