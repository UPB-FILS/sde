import threading

NUM_THREAD = 10

mutex = threading.Lock()

printed = False

def print_text():
    global printed
    mutex.acquire ()
    if not printed:
        printed = True
        print ("printed once")
    mutex.release()

threads = []
for i in range (NUM_THREAD):
    t = threading.Thread (target=print_text)
    threads.append(t)
    t.start()

for i in range (NUM_THREAD):
    threads[i].join()   
