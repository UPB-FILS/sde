import socket
buffersize = 2048
 
# family AF_INET = IP
#   IP address (ex: 192.168.0.12, local 127.0.0.1 - there is no place 127.0.0.1)
#   port (application) (ex: 21 - ftp, 80 - http, 443 - https)
#   source (ip, port) <---> destination (ip, port)
# type: SOCK_STREAM = TCP (verify receive) / SOCK_DGRAM = UDP (best effort)
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
msg = str.encode("15;230;70")
# source ("127.0.0.1", ?) <---> destination ("localhost", 8080)
s.sendto (msg, ("localhost", 8080))
data, from_socket_info = s.recvfrom (buffersize)
print ("Data from {} is {}".format (from_socket_info, data))