import os
import signal
import time

nsigs = 0
rtsigs = 0

stop = False

def signal_handler (sig_number, frame):
	global nsigs, rtsigs, stop
	if sig_number == signal.SIGINT:
		nsigs = nsigs + 1
		time.sleep (0.1)
	if sig_number == 34:
		rtsigs = rtsigs + 1
		time.sleep (0.1)
	elif sig_number == signal.SIGQUIT:
		stop = True

signal.signal (signal.SIGINT, signal_handler)
signal.signal (signal.SIGQUIT, signal_handler)

print ("My PID is {}".format (os.getpid()))

while not stop:
	time.sleep (0.1)

print ("Got {} normal signals".format (nsigs))
print ("Got {} real time signals".format (rtsigs))
