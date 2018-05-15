"""
myapplication/
    spam.py
    bar.py
    grok.py
    __main__.py
bash % python3 myapplication

bash % ls
spam.py bar.py grok.py __main__.py
bash % zip -r myapp.zip *.py

bash % python3 myapp.zip
... output from __main__.py ...

#!/usr/bin/env python3 /usr/local/bin/myapp.zip
"""