import time

def worker0():
    print ('worker 0 start')
    time.sleep (8)
    print ('worker 0 end')

def worker1():
    print ('worker 1 start')
    time.sleep (2)
    print ('worker 1 end')

def worker2():
    print ('worker 2 start')
    time.sleep (6)
    print ('worker 2 end')

def worker3():
    print ('worker 3 start')
    time.sleep (1)
    print ('worker 3 end')

def worker4():
    print ('worker 4 start')
    time.sleep (7)
    print ('worker 4 end')

# main process
def main():
    # TODO - start threads

    time.sleep (3)

    # TODO - wait for threads

main ()
