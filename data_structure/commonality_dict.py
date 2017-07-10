a = {
         'x' : 1,
         'y' : 2,
         'z' : 3
    }

b = {
        'w' : 10,
        'x' : 11,
        'y' : 2
    }

# keys() method of a dictionary returns a keys-view object that exposes the
# keys. keys-view supports common set operations, i.e. unions, intersections
# and differences.

# items() method of a dictionary returns an items-view object, which also
# supports common set operations.

# values() methods of a dictionary does not support set operations since
# the items contained in a values-view object aren't guaranteed to be
# unique.

# Find keys in common
print(a.keys() & b.keys())

# Find keys in a but not in b
print(a.keys() - b.keys())

# Find (key, value) pair in common
print(a.items() & b.items())
