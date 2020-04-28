import socket
 
buffersize = 2048
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind (("0.0.0.0", 8080))

while True:
    data, addr = s.recvfrom(buffersize)
    msg = data.decode("utf-8") 
    numbers = msg.split(';')
    avg = (int(numbers[0]) + int(numbers[1]) + int(numbers[2]))/3
    msg = str.encode ("{}".format (avg))
    s.sendto (msg, addr)