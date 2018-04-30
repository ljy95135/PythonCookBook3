# collections.namedtuple()
# factory: className and list of fieldNames
# not used for update_frequent situation
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)  # Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub.addr)

# it's a sub class of tuple
# can use len or unpack
# can change  tuple<->namedtuple
# use less space than dict but unchangeable

# use ._replace
sub = sub._replace(addr='new_email@example.com')
print(sub)

# default init
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
