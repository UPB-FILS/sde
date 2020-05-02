import socket

import json

buffersize = 3072

s = socket.socket (family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect (("localhost", 8000))
user = {
    "name": "Harry Potter",
    "country": "UK",
    "age": 10
}
data = ""
s.send (('POST /insert HTTP/1.1\r\nContent-Type: application/json\r\nHost: localhost:8000\r\n\r\n{}'.format(json.dumps(user))).encode('ascii'))
data = s.recv(buffersize)
s.close ()
print (data.decode ('ascii'))

s = socket.socket (family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect (("localhost", 8000))
user = {
    "name": "Bender Bending Rodrigues",
    "country": "USA",
    "age": 20
}
s.send (('POST /insert HTTP/1.1\r\nContent-Type: application/json\r\nHost: localhost:8000\r\n\r\n{}'.format(json.dumps(user))).encode('ascii'))
data = s.recv(buffersize)
s.close ()
print (data.decode ('ascii'))

s = socket.socket (family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect (("localhost", 8000))
s.send (('GET / HTTP/1.1\r\nHost: localhost:8000\r\n\r\n').encode('ascii'))
data = s.recv(buffersize)
s.close ()
print (data.decode ('ascii'))
