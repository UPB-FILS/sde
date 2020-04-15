import threading
import random

AVG_COUNT = 10

cond = threading.Condition ()

numbers = []

def generate_rand(seed_nr):
    global numbers
    random.seed (seed_nr)
    numbers.append (random.randint(2000, 3000))

def compute_avg (): 
    sum = 0
    for i in numbers:
        sum = sum + i
    print (sum/AVG_COUNT)

t = threading.Thread(target=compute_avg)
t.start()

for i in range (AVG_COUNT):
    t = threading.Thread(target=generate_rand, args=(i,))
    t.start()