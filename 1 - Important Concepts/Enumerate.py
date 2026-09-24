# Using Enumerate

nums = [2,11,7,15]
thelist = []
for i,n in enumerate(nums):
    thelist.append([n,i])
print(thelist)

# o/p -> [[2, 0], [11, 1], [7, 2], [15, 3]]

thelist.sort()
print(thelist)

# o/p -> [[2, 0], [7, 2], [11, 1], [15, 3]]

# Revised on 24th September 2026