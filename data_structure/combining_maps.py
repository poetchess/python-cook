'''
    You hava multiple dictionaries or mappings that you want to logically
    combine into a single mapping to perform certaion operations.
'''

# Solution 1: Use collections.ChainMap class.

# A ChainMap takes multiple mappings and makes them logically appear as one.
# However, the mappings are not literally merged together.
# If there are duplicate keys, the values from the first mapping get used.
# Operations that mutate the mapping always affect the first mapping listed.

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a, b)
print("c['x']: {}".format(c['x']))
print("c['y']: {}".format(c['y']))
print("c['z']: {}".format(c['z']))

print('a: {}'.format(a))
c['z'] = 10
c['w'] = 40
del c['x']
#del c['y'] KeyError
print('a: {}'.format(a))


# Solution 2: Alternative to ChainMap, we can merge dictionaries using
#   the update() method.

# Shortcoming:
#   Need to make a completely separate dictionary object or destructively alter
#       one of the existing ones.
#   The changed in the original dictionaries won't get reflected in the merged
#       dictionary.

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print('a: {}'.format(a))
print('b: {}'.format(b))
print('merged: {}'.format(merged))
a['x'] = 13
print('a: {}'.format(a))
print('merged: {}'.format(merged))
