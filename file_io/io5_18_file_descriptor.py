import os

fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

f = open(fd, 'wt')
f.write('hello world\n')
f.close()
# if we don't want to close fd
f = open(fd, 'wt', closefd=False)
