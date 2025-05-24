"""
Sets are similar to lists but are unordered and cannot  containduplications
Use curly brackets
"""

my_set = {1,1,2,2,3,4,5}

print(my_set)

for x in my_set:
    print(x)

my_set.discard(3)
print(my_set)

my_set.add(6)
print(my_set)

# tuples are immutable
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(my_tuple[1])



