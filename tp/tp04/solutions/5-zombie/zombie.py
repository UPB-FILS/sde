import os
import sys
import time

try:
	child_pid = os.fork()

	if child_pid == -1:
		print ('fork error')
		sys.exit (-1)
	elif child_pid == 0:
		# child process */
		time.sleep(5)
	else:
		# TODO modify this so that process is not a zombie anymore
		time.sleep(20)
		# parent process does not wait for the child process

except Exception as e:
    print ("Error: {}".format (e))
