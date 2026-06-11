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

# Refer to - DSA-from-the-Start/Important Concepts/Counter.py for Counter implementation

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

# Refer to - DSA-from-the-Start/Important Concepts/BigArray.py for BigArray implementation

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

# Revised on 6th June 2026