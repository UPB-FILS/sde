import os
import signal
import time

stop = False

def signal_handler (sig_number, frame):
	# TODO ask the user if he wants to exit (use input)
	global stop

# TODO set a signal handler for signal SIGINT, SIGQUIT and SIGUSR1

# TODO display PID (hint: getpid)

i=0
while not stop:
	i = i + 1
	print (i)
	time.sleep (1)