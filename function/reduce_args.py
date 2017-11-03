'''
    You hava a callable that you would like to use with some other Python code,
    but it takes too many arguments and causes an exception when called.
'''

# Solution: Use functools.partial() to reduce the number of arguments.

def spam(a, b, c, d):
    print(a, b, c, d)

# partial() allows us to assign fixed values to one or more of the arguments,
# thus reducing the number of arguments needed to be supplied to subsequent calls.
from functools import partial
s1 = partial(spam, 1)
s1(2, 3, 4)
s1(4, 5, 6)

s2 = partial(spam, d=43)
s2(1, 2, 3)
s2(4, 5, 6)

s3 = partial(spam, 1, 2, d=43)
s3(3)
s3(4)

# The sort() method accepts a key argument to customize sorting, but it only
# works with functions that take a single argument. partial() can fix it.
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
import math
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 -y1)

pt = (4, 3)
points.sort(key=partial(distance, pt))
# same effect, but more confusing
#points.sort(key=lambda p: distance(pt, p))
print(points)

# partial() can be used to tweak the argument signatures of callback functions.
def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)

def add(x, y):
    return x + y

if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    # same result, less explicit.
    #p.apply_async(add, (3, 4), callback=lambda result: output_result(result, log))
    p.close()
    p.join()
