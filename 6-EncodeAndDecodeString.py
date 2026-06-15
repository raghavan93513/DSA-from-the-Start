# String manipulation
# Time complexity: O(m+n)
# Space complexity: O(m+n)
# Where m is the sum of lengths of all the strings and n is the number of strings. 

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""

        result,sizes = [],[]

        for s in strs:
            sizes.append(len(s))
        for i in sizes:
            result.append(str(i))
            result.append(",")
        result.append("#")
        result.extend(strs)
        res = ''.join(result)
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return []
        result,sizes,i = [],[],0
        while s[i]!="#":
            j=i
            while s[j]!=",": #Just in case the count has more than 1 digit
                j+=1
            sizes.append(int(s[i:j]))
            i=j+1
        i+=1

        for sz in sizes:
            result.append(s[i:i+sz])
            i = i+sz
        return result

# Optimal and easier solution:
# Time complexity: O(m+n)
# Space complexity: O(m+n)
# Where m is the sum of lengths of all the strings and n is the number of strings.

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""

        result = []

        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return []
        
        result = []
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            i=j+1
            j=i+length
            result.append(s[i:j])
            i=j
        
        return result