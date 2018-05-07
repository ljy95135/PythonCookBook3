a = [1, 2, 3, 4]

for x in reversed(a):
    print(x)


# or __reversed__()
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


print(type(iter(Countdown(30))))  # generator
for rr in Countdown(3):
    print(rr)
for rr in reversed(Countdown(3)):
    print(rr)
