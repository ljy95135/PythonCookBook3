@somedecorator
def add(x, y):
    return x + y


orig_add = add.__wrapped__

# works only when all use right wraps
# no convention for multi decorators

# staticmethod classmethod save orinal func at __func__
