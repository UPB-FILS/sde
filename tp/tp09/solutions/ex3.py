import threading
import random
import time

AVG_COUNT = 10

cond = threading.Condition ()

numbers = []
random.seed (0)
def generate_rand():
    global numbers
    cond.acquire()
    numbers.append (random.randint(2000, 3000))
    if (len(numbers) == AVG_COUNT):
        cond.notify()
    cond.release()

def compute_avg ():
    cond.acquire()
    cond.wait()
    sum = 0
    for i in numbers:
        sum = sum + i
    print (sum/AVG_COUNT)
    cond.release()

t = threading.Thread(target=compute_avg)
t.start()
for i in range (AVG_COUNT):
    t = threading.Thread(target=generate_rand)
    t.start()