import sys


def bad_filename(filename):
    return repr(filename)[1:-1]


def print_file(filename):
    try:
        print(filename)
    except UnicodeEncodeError:
        print(bad_filename(filename))


# print('b\udce4d.txt')
print(repr('b\udce4d.txt')[1:-1])

x = 'b\udce4d.txt'
xx = x.encode(sys.getfilesystemencoding(), errors='surrogateescape')
print(xx)
print(xx.decode('latin-1'))
