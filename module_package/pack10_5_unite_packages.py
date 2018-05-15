"""
foo-package/
    spam/
        blah.py

bar-package/
    spam/
        grok.py
"""

# import sys
# sys.path.extend(['foo-package', 'bar-package'])
# import spam.blah
# import spam.grok

"""
import spam
spam.__path__
_NamespacePath(['foo-package/spam', 'bar-package/spam'])
no spam.__file__ 
spam
<module 'spam' (namespace)>
"""