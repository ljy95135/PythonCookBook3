def add(x: int, y: int) -> int:
    return x + y


def nothing(x, y):
    return x + y


print(add.__annotations__)  # 'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
print(nothing.__annotations__)  # {}
