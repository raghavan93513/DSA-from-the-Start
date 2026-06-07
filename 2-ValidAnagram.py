# Using Sorted method
# Time complexity: O(nlogn + mlogm)
# Space complexity: O(n + m)
# Sorted is small 's'

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

# Using Dictionary frequency counting
# Time complexity: O(n + m)
# Space complexity: O(1) since we have at most 26 different characters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i],0)+1
            dict_t[t[i]] = dict_t.get(t[i],0)+1

        return dict_s == dict_t

# Using Hash Maps - Counter
# Time complexity: O(n + m)
# Space complexity: O(1) since we have at most 26 different characters.
# Counter is capital 'C'

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

# *********************************************************** #

# from collections import Counter
# s="racecar"
# print(Counter(s))
# o/p -> Counter({'r': 2, 'a': 2, 'c': 2, 'e': 1})

# *********************************************************** #

# Using Fixed array frequency counting
# Time complexity: O(n + m)
# Space complexity: O(1) since we have at most 26 different characters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return not any(count) # any(lst) is True if at least one element is non zero and False if all elements are zero
        
        # OR
        # for i in count:
        #     if i>0:
        #         return False
        # return True

# *********************************************************** #

# count = [0] * 26
# print(count)
# o/p -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# *********************************************************** #

# Revised on 6th June 2026