import os
import signal
import sys

# TODO ignore SIGINT signal
signal.signal (signal.SIGINT, signal.SIG_IGN)

if len (sys.argv) < 2:
	print ("Usage: python3 noint.py command ...arguments")
else:
	# TODO run the program spacified in sys.argv[1] with parameters sys.argv[1:] (hint: execvp)
	os.execvp (sys.argv[1], sys.argv[1:])
