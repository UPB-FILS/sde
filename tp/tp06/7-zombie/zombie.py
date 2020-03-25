import os
import time

# TODO create a child process that sleeps for 1 seconds (hint: time.sleep), use ps to get the ppid of the child

pid = os.fork ()
if pid == 0:
	# this is the child
	# TODO exit
	
else:
	# this is the parent
	# TODO just sleep a lot
	
