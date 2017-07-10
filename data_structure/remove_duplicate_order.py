# The purpose of the key argument is to specify a function that coverts
# sequence items into a hashable type to detect duplicate. It mimics
# similar functionality in built-in functions sush as sorted(), min() and
# max().

# The use of a generator function makes the function extremely general
# purpose, not necessarily tied directly to list processing.
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))
