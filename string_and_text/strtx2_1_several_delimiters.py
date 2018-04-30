# re.split
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
# ; , or space with whatever spaces
print(re.split(r'[;,\s]\s*', line))  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
# use parentheses then capture delimiter too
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)  # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
# use delimiters
values = fields[::2]  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
delimiters = fields[1::2] + ['']  # [' ', ';', ',', ',', ',', '']

# Reform the line using the same delimiters
result = ''.join(v + d for v, d in zip(values, delimiters))
print(result)  # asdf fjdk;afed,fjek,asdf,foo

# (?:) shows this is not capture group
print(re.split(r'(?:,|;|\s)\s*', line))  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
