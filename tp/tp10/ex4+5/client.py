import socket
import threading

buffersize = 2048

def connect (msg):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.connect (("localhost", 8000))

    msg = str.encode(msg)
    # send message
    s.send (msg)
    # read message
    data, addr = s.recvfrom (buffersize)
    # close connection
    s.close ()
    output = data.decode ("utf-8")
    print (output)

commands = ["ls", "ls -l", "pwd", "touch test", "ls -l"]
for c in commands:
    t = threading.Thread (target=connect, args=(c, ))
    t.start()