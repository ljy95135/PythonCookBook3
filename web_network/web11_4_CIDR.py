# Classless Inter-Domain Routing
import ipaddress
from socket import socket, AF_INET, SOCK_STREAM

net = ipaddress.ip_network('123.45.67.64/27')
print(net.num_addresses, net[0])
for a in enumerate(net):
    print(a)

a = ipaddress.ip_address('123.45.67.69')
print(a in net)

net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
for a in enumerate(net6):
    print(a)

# ipaddress to str
a = ipaddress.ip_address('127.0.0.1')
s = socket(AF_INET, SOCK_STREAM)
# s.connect((a, 8080))  # Can't convert 'IPv4Address' object to str implicitly
s.connect((str(a), 8080))
