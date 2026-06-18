# Using Sets - Brute Force Solution
# Time complexity: O(n^2)
# Space complexity: O(n)
# Time Limit Exceeded error for large inputs

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        myset = set(nums)
        result = 1
        
        for num in myset:
            streak = 1
            nextnum = num+1
            while nextnum in myset:
                streak+=1
                nextnum+=1
            result = max(streak,result)

        return result

# Using Sets - Optimal Solution
# Time complexity: O(n)
# Space complexity: O(n)
# Where n is the length of the input list.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        myset = set(nums)
        result = 1
        
        for num in myset:
            prevnum = num-1
            if prevnum in myset: #Starting of the sequence would not have a number before it
                continue
            streak = 1
            nextnum = num+1
            while nextnum in myset:
                streak+=1
                nextnum+=1
            result = max(streak,result)

        return result