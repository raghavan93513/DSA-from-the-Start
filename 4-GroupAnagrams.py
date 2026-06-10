# Sorted Approach
# Time complexity: O(n * klogk)
# Space complexity: O(n * k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for word in strs:
            sortedword = ''.join(sorted(word))
            res[sortedword].append(word)
        
        return list(res.values())

# Hash Map Approach using Count Array
# Time complexity: O(n * k)
# Space complexity: O(n * k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(word)
        
        return list(res.values())