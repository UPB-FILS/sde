import time
import threading

def worker0():
    print ('worker 0 start')
    time.sleep (8)
    print ('worker 0 end')

def worker1():
    print ('worker 1 start')
    time.sleep (2)
    print ('worker 1 end')

def worker2():
    print ('worker 2 start')
    time.sleep (6)
    print ('worker 2 end')

def worker3():
    print ('worker 3 start')
    time.sleep (1)
    print ('worker 3 end')

def worker4():
    print ('worker 4 start')
    time.sleep (7)
    print ('worker 4 end')

# main process

threads = []
workers = [worker0, worker1, worker2, worker3, worker4]
for w in workers:
    t = threading.Thread (target=w)
    threads.append (t)
    t.start()
time.sleep (3)

for t in threads:
    if (t.is_alive()):
        t.join()


