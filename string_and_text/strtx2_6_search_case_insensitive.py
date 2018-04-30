#  re.IGNORECASE as flag
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
# UPPER snake, lower snake, Mixed snake
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


# bind the word into that func
def matchcase(word):
    def replace(m):
        replace_text = m.group()
        if replace_text.isupper():
            return word.upper()
        elif replace_text.islower():
            return word.lower()
        elif replace_text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


# UPPER SNAKE, lower snake, Mixed Snake
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
