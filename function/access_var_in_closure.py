'''
    You would like to extend a closure with functions that allow the inner
    variables to be accessed and modified.
'''

# Solution: Using accessor functions and attaching them to the closure as
#           function attributes.

def sample():
    n = 0

    # closure function
    def func():
        print('n=', n)

    # accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


f = sample()
f()
f.set_n(10)
f()
print(f.get_n())


# An extension: use closure to emulate instances of a class.
import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    # redirect special methods 
    def __len__(self):
        return self.__dict__['__len__']()

def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
print(s)

s.push(10)
s.push(20)
s.push('hello')
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())
