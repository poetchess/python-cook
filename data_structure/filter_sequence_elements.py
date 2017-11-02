'''
    You have data inside of a sequence, and need to extract values or reduce
    the sequence using some criteria.
'''

# Solution 1: Use list comprehension.
# Downside: It will produce a large result if the original input is large.
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
positive = [n for n in mylist if n > 0]
negative = [n for n in mylist if n < 0]
print('sequence: {}'.format(mylist))
print('positive: {}'.format(positive))
print('negative: {}'.format(negative))


# Solution 2: Use generator expressions.
# It can produce the filtered values iteratively.
# Remember to drive the iterator.
positive = (n for n in mylist if n > 0)
print(positive) # We get an iterator.
print('positive: {}'.format(list(positive)))


# Solution 3: Wrap the filter logic in its own function and use the BIF filter().
# Use it when filter criteria cannot be easily expressed in a list comprehension
#   or generator expression. i.e. The filtering process involves exception
#   handling.
values = ['1', '2', '-3', '-', '4', 'N/a', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print('The integers are: {}'.format(ivals))


# Solution 4: Use itertools.compress().
# This can be useful if we try to apply the results of filtering one sequence
#   to another related sequence.
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

# First create a boolean selector sequence that indicates which elements
#   satisfy the desired condition.
more5 = [n > 5 for n in counts]

# compress() function picks out the items corresponding to True values.
addr_more5 = list(compress(addresses, more5))
print('Following stores have more than 5 products: {}'.format(addr_more5))
