import time
import threading
import queue
import random

tasks = queue.Queue()

def worker (id):
	global tasks
	exit = False
	print ("Worker {} starting".format (id))
	while not exit:
		task = tasks.get()
		if task == "exit":
			exit = True
		else:
			print ("Worker {} got task {}".format (id, task))
			time.sleep (task)
			print ("Worker {} finished task {}".format (id, task))
		tasks.task_done()
	print ("Worker {} stopped".format (id))

WORKERS=22

workers=[]

for i in range (WORKERS+1):
    t = threading.Thread(target=worker, args=(i,), daemon=True)
    t.start()
    workers.append(t)

for i in range (10):
	tasks.put (random.random()*10)

# for i in range (20):
# 	tasks.put ("exit")

tasks.join ()
# for w in workers:
# 	w.join ()



print ("Main finished")
