import queue
import threading
import math
 
def prime ():
    for nr in range (1,51):
        prime = True
        i = 2
        while prime and i < nr/2:
            if nr % i == 0:
                prime = False
            i = i+1
        if prime:
            q.put (nr)
    q.put ('done')

def square ():
    for nr in range (0, 51):
        if math.sqrt(nr).is_integer():
            q.put (nr)
    q.put ('done')

q = queue.Queue()

t1 = threading.Thread (target=prime)
t1.start ()

t2 = threading.Thread (target=square)
t2.start ()

done = 0
while done < 2:
    item = q.get()
    if (item == 'done'):
        done = done +1
    else:
        print (item)
