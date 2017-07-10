from collections import OrderedDict

# The size of an OrderedDict is more than twice as large as a normal
# dictionary due to the extra linked list that' created. Need to determine
# if the benefits of using it outweighed the extra memory overhead.

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])
