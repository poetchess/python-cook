'''
    You need to execute a reduction function (e.g. sum(), min(), max()), but
    first need to transform or filter the data.
'''

# Solution: Use a generator expression argument to combine a data transformation
#           and reduction.

# Compared to the list comprehension, the generator solution transforms the data
#   iteratively and is much more memory-efficient.

# get the sum
num = [1, 2, 3, 4, 5]
s = sum(x*x for x in num)
print('sum: {}'.format(s))

# Determine if any .py file exist in a directory.
import os
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')


# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65},
]
min_shares = min(s['shares'] for s in portfolio)
print('min shares: {}'.format(min_shares))

# However, sometimes, we need the 'key' argument of certain reduction functions.
min_shares = min(portfolio, key=lambda x: x['shares'])
print('stock with min shares: {}'.format(min_shares))

