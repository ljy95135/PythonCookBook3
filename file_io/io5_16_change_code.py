import urllib.request
import io
import sys

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')

print(text)

# file hierarchy
f = open('sample.txt', 'w')  # _io.TextIOWrappe
# f.buffer _io.BufferedWriter
#  \f.buffer.raw _io.FileIO
# hard to just change the base code
# noinspection PyTypeChecker
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('Jalape\u00f1o')
