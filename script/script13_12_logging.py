# somelib.py
import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


# Example function (for testing)
def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')


"""
>>> import logging
>>> logging.basicConfig()
>>> somelib.func()
CRITICAL:somelib:A Critical Error!
>>>
"""
