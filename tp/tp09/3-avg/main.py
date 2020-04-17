import threading
import random

AVG_COUNT = 10

cond = threading.Condition ()

numbers = []
random.seed(0)

def generate_rand():
    global numbers
    numbers.append (random.randint(2000, 3000))

def compute_avg (): 
    sum = 0
    for i in numbers:
        sum = sum + i
    print (sum/AVG_COUNT)

t = threading.Thread(target=compute_avg)
t.start()

for i in range (AVG_COUNT):
    t = threading.Thread(target=generate_rand)
    t.start()
