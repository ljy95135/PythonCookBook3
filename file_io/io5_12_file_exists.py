import os
import time

print(os.path.exists('/etc/passwd'), os.path.exists('/tmp/spam'))

# False for nonexists
print(os.path.isfile('/etc/passwd'))
print(os.path.isdir('/etc/passwd'))
print(os.path.islink('/usr/local/bin/python3'))
print(os.path.islink('/usr/local/bin/python3'))
print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))
# time.ctime([secs])
time.ctime(os.path.getmtime('/etc/passwd'))
