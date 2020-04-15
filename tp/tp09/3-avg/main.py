import threading
import random

AVG_COUNT = 10

cond = threading.Condition ()


def generate_rand(seed_nr):
    global numbers
    r = random.randint(2000, 3000)
    #TODO - add random numbers to queue

def compute_avg (): 
    #TODO - read numbers from queue

t = threading.Thread(target=compute_avg)
t.start()

for i in range (AVG_COUNT):
    t = threading.Thread(target=generate_rand, args=(i,))
    t.start()


