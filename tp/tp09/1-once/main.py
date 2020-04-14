import threading

NUM_THREAD = 10

printed = False

def print_text():
    print ("printed once")

threads = []
for i in range (NUM_THREAD):
    t = threading.Thread (target=print_text)
    threads.append(t)
    t.start()

for i in range (NUM_THREAD):
    threads[i].join()   
