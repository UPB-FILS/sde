
import time
import threading

def thread_function ():
    for i in range (6):
        print (i)
        time.sleep(1)

t = threading.Thread (target=thread_function, daemon=True)
t.start()

# main process
for i in range (2):
    print ('main {}'.format (i))
    time.sleep (1)
