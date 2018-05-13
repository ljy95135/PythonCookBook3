a = 13
exec('b = a + 1')
print(b)  # 14


# exec get a copy of local vars
# every time call locals will overwrite
def test():
    a = 13
    exec('b = a + 1')
    print(b)  # error when use interactive interpreter


def test():
    a = 13
    loc = locals()  # {'a': 13}
    exec('b = a + 1')
    b = loc['b']
    print(b)


test()


def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)  # x = 1
    locals()  # x=0 overwrites loc
    print(loc)


def test4():
    a = 13
    loc = {'a': a}
    glb = {}
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)
