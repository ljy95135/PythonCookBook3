# bytes -decode> str
# str -encode> bytes
import re
import os

data = b'Hello World'
print(data[0:5])  # b'Hello'
print(data.startswith(b'Hello'))  # True
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = bytearray(b'Hello World')
data[0:5]
print(data.startswith(b'Hello'))  # True
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# can use re
data = b'FOO:BAR,SPAM'
print(re.split(b'[:,]', data))

# index of bytes return int
# can't use format, use encode!
print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

# filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')
print(os.listdir('.'))  # 'jalapeño.txt'
# cant decode with bytes
print(os.listdir(b'.'))  # b'jalape\xc3\xb1o.txt'
