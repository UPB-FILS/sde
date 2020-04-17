import threading
import random
import time

THD_COUNT = 10
barrier = threading.Barrier (THD_COUNT)

def do_sleep(nr):
    print ('Sleep {}'.format(nr))
    time.sleep (nr)
    rc = barrier.wait()
    if rc == 0:
        print ('Passed barried')

threads = []
random.seed (0)
for i in range (THD_COUNT):
    nr = random.randint (0,10)
    t = threading.Thread (target=do_sleep, args=(nr,))
    threads.append (t)
    t.start()
for i in range (THD_COUNT):
    threads[i].join()

