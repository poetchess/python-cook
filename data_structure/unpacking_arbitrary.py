from statistics import mean

# variable 'middle' will always be a list.
def drop_first_last(grades):
    first, *middle, last = grades
    return mean(middle)

grades = [90, 85, 95, 98, 100, 96, 99, 80, 98]
print('grades are: {}'.format(grades))
print('The average of the middle is: {:.3f}'.format(drop_first_last(grades)))

# The star syntax is useful when iterating over a sequence of tuples of varying length.
records = [
            ('foo', 1, 2),
            ('bar', 'hello'),
            ('foo', 3, 4),
          ]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


