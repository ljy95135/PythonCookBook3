from xml.etree.ElementTree import Element, tostring


def dict_to_xml(tag, d):
    """
    Turn a simple dict of key/value pairs into XML
    """
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)
print(tostring(e))  # b'<stock><name>GOOG</name><shares>100</shares><price>490.1</price></stock>'

# add attr
e.set('_id', '1234')
# use OrderedDict to make xml children ordered
#  xml.sax.saxutils:  escape, unescape
