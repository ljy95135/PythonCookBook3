# default val must be immutable or results in trouble

def spam(a, b=42):
    print(a, b)


_non_value = object()


def spam2(a, b=_non_value):
    if b is _non_value:
        print(a, 'no value b')


spam(1)
spam(1, 2)
