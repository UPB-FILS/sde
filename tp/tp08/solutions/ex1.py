import threading
def worker():
    id = threading.get_ident()
    for i in range (6):
        print ('{} {}'.format (id, i))

for i in range (5):
    t = threading.Thread (target=worker)
    t.start()