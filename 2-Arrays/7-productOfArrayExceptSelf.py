# Brute Force Approach
# Time complexity: O(n^2)
# Space complexity: O(n)
# Wont work for large arrays

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i!=j:
                    product = product*nums[j]
            answer.append(product)
        return answer


# Better Approach
# Time complexity: O(n^2)
# Space complexity: O(n)
# Works for large arrays

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for i in nums:
            product = product*i
        
        answer = [product]*len(nums)

        for i in range(len(answer)):
            if nums[i]!=0:
                answer[i]=int(answer[i]/nums[i])
            else:
                prod = 1
                for j in range(len(nums)):
                    if i!=j:
                        prod=prod*nums[j]
                answer[i]=prod
        
        return answer

# Prefix and Suffix Product
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        prefix = [0]*n
        suffix = [0]*n

        prefix[0]=suffix[n-1]=1

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums [i+1]
        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer