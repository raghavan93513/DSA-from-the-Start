from collections import defaultdict

rows = defaultdict(set)

rows[0].add("5")
rows[0].add("3")
rows[1].add("6")
rows[2].add("8")
rows[2].add("5")

print(rows)

# o/p -> defaultdict(<class 'set'>, {0: {'5', '3'}, 1: {'6'}, 2: {'8', '5'}})   

# or

# {
#     0: {"5", "3"},
#     1: {"6"},
#     2: {"8", "5"}
# }

print(rows[0])
# o/p -> {'5', '3'}

print(rows[1])
# o/p -> {'6'}

print(rows[2])
# o/p -> {'8', '5'}

print(rows[3])
# o/p -> set()

Other types of defaultdict:

defaultdict(list)
defaultdict(int)
defaultdict(float)
defaultdict(str)
defaultdict(bool)
defaultdict(tuple)
defaultdict(dict)

mydict = defaultdict(dict)
mydict[0] = {"a": 1, "b": 2}
mydict[1] = {"c": 3, "d": 4}
print(mydict)
# o/p -> defaultdict(<class 'dict'>, {0: {'a': 1, 'b': 2}, 1: {'c': 3, 'd': 4}})

# or

# {
#     0: {"a": 1, "b": 2},
#     1: {"c": 3, "d": 4}
# }