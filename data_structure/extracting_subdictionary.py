'''
    You want to make a dictionary that is a subset of another dictionary.
'''

# Solution: Use dictionary comprehension.
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

p1 = { key:value for key, value in prices.items() if value > 200 }
print('Stock price larger than $200: {}'.format(p1))

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = { key:value for key, value in prices.items() if key in tech_names}
print('Overlapped companies: {}'.format(p2))

p3 = { key:prices[key] for key in tech_names if key in prices }
print(p3)

# Another way to get the same result of p2. But it is slower.
p4 = { key:prices[key] for key in prices.keys() & tech_names }
print(p4)