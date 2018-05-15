"""
mypackage/
    __init__.py
    A/
        __init__.py
        spam.py
        grok.py
    B/
        __init__.py
        bar.py
"""

# in mypackage.A.spam
# from . import grok
# from ..B import bar
# python3 -m mypackage.A.spam
