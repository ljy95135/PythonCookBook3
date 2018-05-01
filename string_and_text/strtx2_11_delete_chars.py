# string.r|lstrip strip
s = ' hello world \n'
print(s.strip())  # hello world
t = '-----hello====='
print(t.lstrip('-'))  # hello=====
print(t.strip('-='))  # hello


# re or string.replace for inner chars
# wither other itertools
def read(filename):
    with open(filename) as f:
        lines = (line.strip() for line in f)  # generator
    for line in lines:
        print(line)
