# str. ljust rjust center
text = 'Hello World'

# ljust(width[, fillchar])
print(text.ljust(20))  # 'Hello World         '
print(text.rjust(20))  # right align
print(text.center(20))
print(text.rjust(20, '='))  # =========Hello World
print(text.center(20, '*'))  # ****Hello World*****

# use built-in format
print(format(text, '>20'))  # right align
print(format(text, '<20'))  # left
print(format(text, '^20'))  # center
# fillin char
# =>20s s is default string format
print(format(text, '=>20'))  # right align
print(format(text, '=<20'))  # left
print(format(text, '=^20'))  # center

# str.format :format_spec
print('{:>10s} {:>10s}'.format('Hello', 'World'))
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))  # 1.23
