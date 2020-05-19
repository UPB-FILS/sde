import socket
 
buffersize = 2048
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind (("0.0.0.0", 8080))

while True:
    print ("Waiting for message")
    data, from_socket_info = s.recvfrom(buffersize)
    msg = data.decode("utf-8") 
    print ("Got message from {}  {}".format(from_socket_info, data))
    numbers = msg.split(';')
    avg = (int(numbers[0]) + int(numbers[1]) + int(numbers[2]))/3
    msg = str.encode ("{}".format (avg))
    # source ("localhost", 8080) <---> destination ("127.0.0.1", ?)
    s.sendto (msg, from_socket_info)