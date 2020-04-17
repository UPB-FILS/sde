import threading

magic_number = 0

mutex = threading.Lock()

def reverse(num):
    nr = 0
    while num > 0:
        nr = nr*10 + (num % 10)
        num = int (num / 10 )
    return nr

def find_magic_number(min, max): 
    global magic_number
    for i in range (min, max):
        rev = reverse(i)
        if rev == i:
            mutex.acquire()
            if magic_number == 0:
                magic_number = i
            mutex.release()
            break

t1 = threading.Thread(target=find_magic_number, args=(1000, 2000,))
t1.start()

t2 = threading.Thread(target=find_magic_number, args=(2000, 3000,))
t2.start()

t1.join()
t2.join()

print (magic_number)
