import os
import glob  # Unix style pathname pattern expansion
import fnmatch

names = os.listdir('.')
print(names)  # basename
names = [name for name in os.listdir('somedir')
         if os.path.isfile(os.path.join('somedir', name))]
dirnames = [name for name in os.listdir('somedir')
            if os.path.isdir(os.path.join('somedir', name))]
pyfiles = [name for name in os.listdir('somedir')
           if name.endswith('.py')]
pyfiles2 = glob.glob('somedir/*.py')
pyfiles3 = [name for name in os.listdir('somedir')
            if fnmatch.fnmatch(name, '*.py')]

# os.stat
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]
for name, size, mtime in name_sz_date:
    print(name, size, mtime)

file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
