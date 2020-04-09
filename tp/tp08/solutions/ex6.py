import os
import threading
import queue

def worker ():
    while True:
        line = q1.get()
        if line != 'exit':
            cmd = line.split()
            pid = os.fork()
            if pid == 0:
                os.execvp (cmd[0], cmd)
            else:
                os.waitpid(pid, 0)
                q2.put ('done')
        else:
            q2.put ('done')
            break

q1 = queue.Queue()
q2 = queue.Queue()

t = threading.Thread (target=worker)
t.start()

while True:
    cmd = input("> ")
    q1.put (cmd)
    q2.get()
    if cmd == 'exit':
        exit (0)

