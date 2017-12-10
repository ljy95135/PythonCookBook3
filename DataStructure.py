from collections import deque
import heapq

# 1.1-1.2 * to unpack the iterable
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
# 1.3 reserve last N elements
# collections.deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


# delete oldest item in deque
# appendleft
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)  # 2 3 4
q.pop()  # 4 -> 2 3
q.popleft()  # 2 -> 3
print(q)

#################################################
# 1.4 find max or min N elements
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)
print(nums)  # [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
print(heapq.heappop(nums))  # nlen(nums)-1
print(nums)


#################################################
# 1.5 Priority Queue
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

# higher priority first
# return the smallest: 1. -priority 2. index
print(q.pop())  # bar
print(q.pop())  # spam
print(q.pop())  # foo

print((1, "name") < (2, "big"))  # True
