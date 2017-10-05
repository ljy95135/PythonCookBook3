# 1.1 * to unpack the iterable
p = (4, 5)
x, y = p
assert x == 4 and y == 5

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
assert name == 'ACME' and date == (2012, 12, 21)

s = 'Hi'
a, _ = s
assert a == 'H'

first, *middle, last = 'abcde'
assert first == 'a' and last == 'e'
assert middle == ['b', 'c', 'd']

assert sum([1, 2, 3, 4]) == 10
assert len([1, 2, 3, 4]) == 4

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x1, y1):
    print('foo', x1, y1)


def do_bar(s1):
    print('bar', s1)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
assert uname == 'nobody', "It should be nobody"
assert homedir == '/var/empty'

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
assert name == 'ACME' and year == 2012

#################################################
# reserve last N elements
