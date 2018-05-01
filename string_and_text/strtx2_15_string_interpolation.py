s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))  # 'Guido has 37 messages.'

name = 'Guido'
n = 37
print(s.format_map(vars()))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
print(vars(a))  # {'name': 'Guido', 'n': 37}
print(s.format_map(vars(a)))


# good for miss some value
class Safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


example = Safesub()
example.update({'name': 'Guido'})
print(s.format_map(example))  # Guido has {n} messages.

# sys._getframe(1).f_locals
# or use '%(name) has %(n) messages.' % vars()
# s = string.Template('$name has $n messages.')
# s.substitute(vars())
