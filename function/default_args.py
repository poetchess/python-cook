'''
    You want to define a function or method where one or more of the arguments
    are optional and have a default value.
'''

# Solution: 
#   Assign values in the definition and make sure that default arguments
#       appear last.
#   If the default value is supposed to be a mutable container, use None
#       as the default and check whether is is None

# Values assigned as a default are bound only once at the time of function
#   definition.

# Values assigned as defaults should always be immutable objects, such as
#   None, True, False, numbers or strings.

def spam_1(a, b=43):
    print(a, b)

# The use of the 'is' operator when testing for None is critical.It is not
#   correct to use 'if not b' because many other objects (e.g. zero-length strings,
#   lists, tuples, dicts, etc.) evaluate to False.
def spam_2(a, b=None):
    if b is None:
        b = []

# Just want to test whether an optional argument was given an value.
_no_value = object()
def spam_3(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')

# There exists difference.
spam_3(1)
spam_3(1, None)


