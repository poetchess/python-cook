'''
    You want to access the elements in a list or tuple by name.
'''

# collections.namedtuple() is actually a factory method that returns a subclass
# of the standard Python tuple type. It needs a type name, and the fields name.
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-09')

print(sub)
print(sub.addr)
print(sub.joined)

# An instance of a namedtuple is interchangeable with a tuple and supports all
# the tuple operations.
print(len(sub))
addr, joined = sub
print(addr)
print(joined)


# The major use case for the namedtuple is to decoupling the code from the 
# position of the elements.

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Supposed that the recoreds are retrieved using a database call.
# Code using ordinary tuple
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# Code using namedtuple
def compute_cost_named(records):
    total = 0.0
    for rec in records:
        # Convertion to Stock namedtuple can be avoided if the records sequence
        # already contained such instances.
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# Possible use of a namedtuple is as a replacement for a dictory, which requires
# more space to store. But namedtuple is immutable, and if you need to change 
# any of the attributes, use the _replace() method of a namedtuple instance,
# which will make an entirely new namedtuple with specified values replaced.    
# If the goal is to define an efficient data structure where you will changing
# various instance attributes, consider define a class using __slots__ instead.
stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
