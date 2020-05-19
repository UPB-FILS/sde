import socket
import json

buffersize = 3072

s = socket.socket (family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect (("api.ipify.org", 80))

s.send ("GET /?format=json HTTP/1.0\r\n".encode ())
s.send ("Host: api.ipify.org\r\n".encode ())
# s.send ("Connection: close\r\n".encode ())
s.send ("\r\n".encode ())

data = s.recv (buffersize)
elements = data.decode ().split ("\r\n")
resultcode = elements[0].split (" ")
print (resultcode)
if resultcode[1] == "200":
    obj = json.loads (elements[-1])
    print (obj["ip"])
else:
    print ("http error {}".format (" ".join (resultcode[2:])))
