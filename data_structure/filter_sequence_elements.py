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
