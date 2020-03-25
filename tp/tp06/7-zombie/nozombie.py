import os
import time
import signal

# TODO create a child process that sleeps for 1 seconds (hint: time.sleep), use ps to get the ppid of the child

# TODO handle SIGCHLD and print a message when a child exists

def child_handler (sig_number, frame):
	# TODO use os.wait to get the pid of the child and the exit status
	# exit status is the higher 8 bytes (>>8) of the returned status
	pass

pid = os.fork ()
if pid == 0:
	# this is the child
	# TODO exit

	# TODO 2 change exit status
else:
	# this is the parent
	# TODO just sleep a lot
