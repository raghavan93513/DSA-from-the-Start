# heapq = heap queue algorithm

# heapq implements a min-heap by default. That means the smallest value is always at the top, at index 0

import heapq
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
print(heap[0])

# o/p -> 1 -> 1 is the smallest value in the heap

# For a max-heap, you want the largest value at the top. Python’s heapq is a min-heap by default, so the common trick is to store values as negative numbers.

import heapq
heap = []
heapq.heappush(heap, -5)
heapq.heappush(heap, -2)
heapq.heappush(heap, -8)
heapq.heappush(heap, -1)
print(-heap[0])

# o/p -> 8 -> 8 is the largest value in the heap