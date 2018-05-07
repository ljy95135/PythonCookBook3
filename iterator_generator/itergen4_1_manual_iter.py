def manual_iter(it):  # for a iterator
    # try except
    try:
        while True:
            _ = next(it)
    except StopIteration:
        pass
    # mark
    while True:
        line = next(it, None)
        if line is None:
            break


items = [1, 2, 3]
it = iter(items)
print(type(it))  # list_iterator
print(next(it, None))
print(next(it, None))
print(next(it, None))
print(next(it, None))  # None
