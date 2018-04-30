from urllib.request import urlopen
import re

filename = 'spam.txt'
print(filename.endswith('.txt'))  # True
print(filename.startswith('file:'))  # False

# can use a tuple of str as param
filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
print([name for name in filenames if name.endswith(('.c', '.h'))])  # ['foo.c', 'spam.c', 'spam.h']
print(any(name.endswith('.py') for name in filenames))  # True


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


# or use slice
# or use re: slower than starts with
url = 'http://www.python.org'
result = re.match('http:|https:|ftp:', url)
print(result.group())  # http: same as result[0]
