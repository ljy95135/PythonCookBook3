import tempfile

# mkstemp mkdtemp

with tempfile.TemporaryFile('w+t') as f:
    f.write('Hello World\n')
    f.write('Testing\n')
    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
# f is destroyed
# or
# f = TemporaryFile('w+t')
# do something
# f.close()

# can use prefix='mytemp', suffix='.txt', dir='/tmp'
with tempfile.NamedTemporaryFile('w+t') as f:
    print(f.name)  # ...\AppData\Local\Temp\tmple6cn906

# not delete
# with tempfile.NamedTemporaryFile('w+t', delete=False) as f:
#     print(f.name)

with tempfile.TemporaryDirectory() as dirname:
    print(dirname)
# dir and all contents are destroyed
