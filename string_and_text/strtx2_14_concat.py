# join
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))  # Is Chicago Not Chicago?

# or just a + ' ' +b
# or for string literal
a = 'a''b'
print(a)  # ab

# but remember memory cost for +
# not use concat in print!
print('a', 'b', 'c', sep=':')  # a:b:c


# use with IO
# for short string version 1 is better (IO is slow)
# for huge string version 2 is better (not use extra space for string concat)
def file_write(name):
    chunk1 = '1'
    chunk2 = '2'
    f = open(name)
    # Version1
    f.write(chunk1 + chunk2)
    # Version2
    f.write(chunk1)
    f.write(chunk2)


# use generator func
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


text = ' '.join(sample())
print(text)  # or f.write(part) and for part in sample()


# a mix plan
# write every maxsize or at the end
# some part can be written several times
def combine(source, maxsize):
    combine_parts = []
    size = 0
    for combine_part in source:
        combine_parts.append(combine_part)
        size += len(combine_part)
        if size > maxsize:
            yield ''.join(combine_parts)
            combine_parts = []
            size = 0
        yield ''.join(combine_parts)


with open('filename', 'w') as file:
    for part in combine(sample(), 32768):
        file.write(part)
