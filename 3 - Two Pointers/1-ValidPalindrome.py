# Brute Force Approach
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        comparestring = ""
        for char in s:
            if char.isalnum(): #Checks if it is alpha numerical
                comparestring += char.lower()
        print(comparestring)
        return comparestring == comparestring[::-1]

# Two Pointers Approach
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# Need to implement the isalnum function and should not use the built in function:

def Checkifalnum(self, c: str) -> bool:        # Dont forget the self keyword and datatypes, then only colon cp,es
    return (ord('A') <= ord(c) <= ord('Z') or  # 'or' should not be in caps
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))    # The number should be in quotes