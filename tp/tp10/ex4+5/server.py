import socket
import os
import threading

buffersize = 2048

def worker (conn):
    while True:
        try:
            data = conn.recv(buffersize)
        except:
            break
        msg = data.decode("utf-8") 
        cmd = msg.split()
        print (cmd)
        r, w = os.pipe() 
        pid = os.fork()
        if pid == 0:
            os.close (r)
            os.dup2 (w, 1)
            os.dup2 (w, 2)
            os.execvp (cmd[0], cmd)
        else:
            os.close(w)
            os.waitpid(pid, 0)
            buffer = os.read (r, buffersize)
            conn.send (buffer)
            conn.close ()

s = socket.socket (family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind (("0.0.0.0", 8000))
s.listen (0)
while True:
    print ("Waiting for connections")
    client_socket, addr = s.accept ()
    print ("Connected {}".format (addr))
    t = threading.Thread (target=worker, args=(client_socket, ))
    t.start()