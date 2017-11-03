'''
    You want a function to only accept certain arguments by keyword.
'''

# Solution: Place the keyword argument after a * argument or a single unnamed *.
# Advantage of keyword-only arguments:
#   Enforce code clarity when specifying optional function arguments.

def recv(maxsize, *, block):
    'Receive a message'
    pass

#recv(1024, True)    # TypeError
recv(1024, block=True)

# 'clip' occurs after * argument, therefor, it is a keyword-only argument.
def minium(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minium(1, 5, 2, -5, 10))
print(minium(1, 5, 2, -5, 10, clip=0))
