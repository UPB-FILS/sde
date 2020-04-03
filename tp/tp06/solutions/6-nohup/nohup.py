import os
import signal
import sys

if len (sys.argv) < 2:
	print ("Usage: python3 nohup.py command ...arguments")
else:
	# TODO redirect output to to nohup.out
	f = os.open ("nohup.out", os.O_CREAT | os.O_TRUNC | os.O_RDWR, 0o644)
	os.dup2 (f, 1)
	os.close (f)

	# TODO ignore SIGHUP signal
	signal.signal (signal.SIGHUP, signal.SIG_IGN)
	# TODO run the program spacified in sys.argv[1] with parameters sys.argv[1:] (hint: execvp)
	os.execvp (sys.argv[1], sys.argv[1:])
