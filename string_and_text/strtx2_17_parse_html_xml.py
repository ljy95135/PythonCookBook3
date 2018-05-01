#  &entity; or &#code; into char
# from html.parser import HTMLParser
import html
from xml.sax.saxutils import unescape

s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))  # &quot;&lt;
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))  # b'Spicy Jalape&#241;o'

# unescape
s = 'Spicy &quot;Jalape&#241;o&quot.'
# p = HTMLParser()
# # should use html.unescape
# p.unescape(s)
print(html.unescape(s))
t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))
