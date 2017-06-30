# Any sequence or iterable can be unpacked into variables using a simple assigement.
# The only requirement is that the number of variables and structure match the sequence.

print('unpacking a tuple:')
p = (4, 5)
x, y = p
print(x)
print(y)

print('unpacking a List:')
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)

# ignore certain values
name, shares, price, (year, month, _) = data
print(year)
print(month)
