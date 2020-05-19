import socket
import json

buffersize = 3072

s = socket.socket (family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind (("0.0.0.0", 8000))
s.listen (0)

users = []

def get_body (msg):
    lines = msg.split ("\r\n")
    return lines.pop()

def return_error (conn):
    conn.send (('HTTP/1.0 500 Bad request\r\nConnection: close\r\n\r\n').encode('ascii'))

while True:
    conn, addr = s.accept ()

    data = conn.recv(buffersize)

    msg = data.decode("utf-8")

    if (msg[0:3] == "GET") and (msg[4:6] == "/ "):
        conn.send (('HTTP/1.0 200 OK\r\nContent-type:application/json\r\nConnection: close\r\n\r\n{}'.format(json.dumps(users))).encode('ascii'))
    elif (msg[0:3] == "GET") and (msg[4:12] == "/person "):
        conn.send (('HTTP/1.0 200 OK\r\nContent-type:text/html\r\nContent-type:application/json\r\nConnection: close\r\n\r\n{}'.format(json.dumps({
"name" : "Harry Potter",
"age" : 10,
"country" : "UK"
}))).encode('ascii'))
    elif (msg[0:4] == "POST") and (msg[5:12] == "/"):
        # print (msg)
        body = get_body (msg)
        print ('('+body+')')
        if body == "age":
            response = 10
        if body == "name":
            response = "Raluca Manea"
        if body == "country":
            response = "Romania"
        try:
            # users.append (json.loads(body))
            conn.send (('HTTP/1.0 200 OK\r\nContent-type:text/plain\r\nConnection: close\r\n\r\n{}').format (response).encode ('ascii'))
        except:
            return_error(conn)
    elif (msg[0:4] == "POST") and (msg[5:12] == "/insert"):
        body = get_body (msg)
        try:
            users.append (json.loads(body))
            conn.send (('HTTP/1.0 200 OK\r\nConnection: close\r\n\r\n').encode('ascii'))
        except:
            return_error(conn)
    else:
        return_error(conn)

    conn.close()