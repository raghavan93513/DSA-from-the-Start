# Using Hash Map and Sorting
# Time complexity: O(nlogn)
# Space complexity: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mydict = Counter(nums)
        # mydict = {}
        # for i in range(len(nums)):
        #     mydict[nums[i]] = mydict.get(nums[i],0)+1

        mylist = []
        for num,rep in mydict.items(): 
        #enumerate(mydict) for index and value, mydict.items() for key and value
            mylist.append([rep,num])
        
        mylist.sort()
        result = []
        while len(result)<k:
            result.append(mylist.pop()[1])

        return result

# Refer to - DSA-from-the-Start/Important Concepts/Heap.py for heap implementation

# Using Min-Heap
# Time complexity: O(nlogk)
# Space complexity: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mydict = Counter(nums)
        # mydict = {}
        # for i in range(len(nums)):
        #     mydict[nums[i]] = mydict.get(nums[i],0)+1

        heap = []
        for num,freq in mydict.items():
        # Can even do mydict.keys() and iterate using mydict[i] and i
            heapq.heappush(heap, (freq,num))
            if len(heap)>k:
                heapq.heappop(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

# Using Bucket Sort
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mydict = Counter(nums)
        # mydict = {}
        # for i in range(len(nums)):
        #     mydict[nums[i]] = mydict.get(nums[i],0)+1

        totalfreq = [[] for i in range(len(nums)+1)]

        for num,freq in mydict.items():
            totalfreq[freq].append(num)

        result = []
        for i in range(len(totalfreq)-1,0,-1):
            for num in totalfreq[i]:
                result.append(num)
            if len(result)==k:
                return result

        return []