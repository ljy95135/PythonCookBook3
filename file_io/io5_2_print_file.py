def write():
    with open('d:/work/test.txt', 'wt') as f:
        # only for text mode
        print('Hello World!', file=f)
