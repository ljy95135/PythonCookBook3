"""
mypackage/
    __init__.py
    somedata.dat
    spam.py

# spam.py
import pkgutil  # get bytes
data = pkgutil.get_data(__package__, 'somedata.dat')
"""