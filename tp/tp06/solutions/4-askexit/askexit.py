import os
import signal
import time

stop = False

def signal_handler (sig_number, frame):
	# TODO ask the user if he wants to exit (use input)
	global stop
	answer = input ("Do you want to exit? (y/n)")
	print (answer)
	if answer == "y":
		stop = True
	pass

# TODO set a signal handler for signal SIGINT, SIGQUIT and SIGUSR1
signal.signal (signal.SIGINT, signal_handler)
signal.signal (signal.SIGQUIT, signal_handler)
signal.signal (signal.SIGUSR1, signal_handler)

# TODO display PID
print ("Muy PID is {}".format (os.getpid()))

i=0
while not stop:
	i = i + 1
	print (i)
	time.sleep (1)