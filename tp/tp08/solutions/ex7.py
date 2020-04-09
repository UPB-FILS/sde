import os
import threading
import queue
import random

def worker ():
    maxnum = 0
    while True:
        item = q1.get()
        if item == 'done':
            q2.put (maxnum)
            break
        elif item > maxnum:
                maxnum = item
        q1.task_done()


q1 = queue.Queue()
q2 = queue.Queue()

numbers = []
random.seed (1)

for i in range (3):
    t = threading.Thread(target=worker)
    t.start()

for i in range (100000):
    numbers.append (random.randint(0, 100000000))
for nr in numbers:
    q1.put (nr)

q1.join ()

max_numbers = []
for i in range (3):
    q1.put ('done')
    max_numbers.append (q2.get())

print (max(max_numbers))