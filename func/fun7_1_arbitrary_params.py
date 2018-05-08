import html


# positional vars
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2))
print(avg(1, 2, 3, 4))


# keyword vars
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


# <item size="large" quantity="6">Albatross</item>
print(make_element('item', 'Albatross', size='large', quantity=6))
# <p>&lt;spam&gt;</p>
print(make_element('p', '<spam>'))


# combine
def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict


# positional *args only-keyword **kwargs
# noinspection PyUnusedLocal
def a(x, *args, y):
    pass


# noinspection PyUnusedLocal
def b(x, *args, y, **kwargs):
    pass
