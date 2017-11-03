'''
    You have a class that only defines a single method beside __init__(). However,
    to simplify the code, you would like to use a simple function.
'''

# Solution: Single-method classes can be turned into functions using closures.

from urllib.request import urlopen
class UrlTemplate:
    def __init__(self, template):
        self.template = template
    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM, AAPL, FB', fields='sl1c1v'):
    print(line.decode('urf-8'))


# Replaced with a much simpler function:
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM, AAPL, FB', fields='sl1c1v'):
    print(line.decode('urf-8'))


