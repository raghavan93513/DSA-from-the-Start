# Using Sets
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for i in range(len(nums)):
            if nums[i] in my_set:
                return True
            else:
                my_set.add(nums[i])
        return False

# Using Logic and Sets
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        return False