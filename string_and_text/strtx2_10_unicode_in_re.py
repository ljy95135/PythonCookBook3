# better to use third library
import re

num = re.compile('\d+')
print(num.match('123').group())

# Arabic digits
s1 = '\u0661\u0662\u0663'
print(num.match(s1).group())

# Chinese digits
print(num.match('一二三'))  # None

# Arabic characters
# '[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+'

# special cases
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s).group(0))  # match
print(pat.match(s.upper()))  # Doesn't match
print(s.upper())  # STRASSE
