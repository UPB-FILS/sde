import sys
import threading

def worker(nr):
    if nr%2 == 0:
        print ('par')
    else:
        print ('impar')

args = sys.argv[1:]
for i in args:
    nr = int (i)
    t = threading.Thread (target=worker, args=(nr,))
    t.start()
