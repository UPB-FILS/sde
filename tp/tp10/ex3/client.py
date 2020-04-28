import socket
buffersize = 2048
 
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
msg = str.encode("15;230;70")
s.sendto (msg, ("localhost", 8080))
data, addr = s.recvfrom (buffersize)
print ("Data from {} is {}".format (addr, data))