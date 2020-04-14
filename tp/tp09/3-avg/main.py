import threading
import random

AVG_COUNT = 10

semaphore = threading.Semaphore (2)

min = 0
max = 0

def generate_min():
    global min
    random.seed (0)
    min = random.randint(1000, 2000)

def generate_max():
    global max
    random.seed (0)
    max = random.randint(2000, 3000)


for i in range (AVG_COUNT):
    t_min = threading.Thread (target=generate_min)
    t_max = threading.Thread (target=generate_max)
    t_min.start()
    t_max.start()

    sum = 0
    count = t_max - t_min
    for i in range (min,max):
        sum = sum + i
    print (sum/count)