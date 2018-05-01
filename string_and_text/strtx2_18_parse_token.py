import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# not documented but can run
scanner = master_pat.scanner('foo = 42')
print(type(scanner))  # _sre.SRE_Scanner
mat = scanner.match()
print((mat.lastgroup, mat.group()))
mat = scanner.match()
print((mat.lastgroup, mat.group()))
mat = scanner.match()
print((mat.lastgroup, mat.group()))
mat = scanner.match()
print((mat.lastgroup, mat.group()))
mat = scanner.match()
print((mat.lastgroup, mat.group()))
mat = scanner.match()
print(mat)


def generate_tokens(pat, text_token):
    Token = namedtuple('Token', ['type', 'value'])
    token_scanner = pat.scanner(text_token)
    for m in iter(token_scanner.match, None):
        yield Token(m.lastgroup, m.group())


# noinspection PyTypeChecker
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)
# Produces output
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')
