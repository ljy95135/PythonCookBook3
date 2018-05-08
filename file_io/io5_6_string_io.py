import io

s = io.StringIO()
print(s.write('Hello World\n'))  # return 12
print('This is a test', file=s)
s.seek(0)  # change position
print(s.read(4))
print(s.getvalue())
print(s.read())
