import os
import signal
import sys

if len (sys.argv) < 2:
	print ("Usage: python3 nohup.py command ...arguments")
else:
	# TODO redirect output to to nohup.out

	# TODO ignore SIGHUP signal
	
	# TODO run the program spacified in sys.argv[1] with parameters sys.argv[1:] (hint: execvp)
	
