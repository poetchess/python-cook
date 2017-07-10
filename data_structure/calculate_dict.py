prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
        }

# zip() creates an iterator that can only be consumed once.
# zip() inverts the dictionary into a sequence of tuples.
# In this example, if the values are the same, keys will be compared.
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(min_price)
print(max_price)
print(prices_sorted)
