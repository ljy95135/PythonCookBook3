"""
bash % env PYTHONPATH=/some/dir:/other/dir python3
Python 3.3.0 (default, Oct 4 2012, 10:17:33)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/some/dir', '/other/dir', ...]
>>>

in site-packages
# myapplication.pth
/some/dir
/other/dir

or
import sys
sys.path.insert(0, '/some/dir')
sys.path.insert(0, '/other/dir')

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname('__file__')), 'src'))
"""
