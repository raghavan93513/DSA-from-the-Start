# heapq = heap queue algorithm

# heapq implements a min-heap by default. That means the smallest value is always at the top, at index 0

import heapq
heapa = []
heapq.heappush(heapa, 5)
heapq.heappush(heapa, 2)
heapq.heappush(heapa, 8)
heapq.heappush(heapa, 1)
print(heapa[0]) # o/p -> 1 -> 1 is the smallest value in the heap

print(heapq.heappop(heapa)) # o/p -> 1
print(heapq.heappop(heapa)) # o/p -> 2
print(heapa[0]) # o/p -> 5

# For a max-heap, you want the largest value at the top. Python’s heapq is a min-heap by default, so the common trick is to store values as negative numbers.

import heapq
heapb = []
heapq.heappush(heapb, -5)
heapq.heappush(heapb, -2)
heapq.heappush(heapb, -8)
heapq.heappush(heapb, -1)
print(-heapb[0]) # o/p -> 8 -> 8 is the largest value in the heap

# Revised on 24th September 2026