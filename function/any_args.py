'''
    You want to write a function that accepts any number of input arguments
'''

# Solution: 
#   Use * argument to accept any number of positional arguments.
#   Use ** argument to accept any number of keyword arguments.

# 'rest' is a tuple of all the extra positional arguments.
def avg(first, *rest):
    return (first + sum(rest))/(1 + len(rest))

print('avg(1, 2): {}'.format(avg(1,2)))
print('avg(1, 2, 3, 4): {}'.format(avg(1,2,3,4)))


import html
# 'attrs' is a dictionary holding the keyword arguments if any.
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                    name=name,
                    attrs=attr_str,
                    value=html.escape(value))
    return element

print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))


def anyargs(*args, **kwargs):
    print(args)     # a tuple
    print(kwargs)   # a dict


# A * argument can only appear as the last positional argument in a function
# definition. A ** argument can only appear as the last argument.

# Arguments can still appear after a * argument. Such arguments are called
# keyword-only arguments.
def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass
