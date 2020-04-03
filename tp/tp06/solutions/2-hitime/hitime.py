import signal
import os
import sys

signals = [signal.SIGSEGV, signal.SIGTSTP, signal.SIGTTIN, signal.SIGTTOU, signal.SIGURG, signal.SIGXCPU]

stop = False

def signal_handler (sig_number, frame):
	global stop
	if sig_number == signal.SIGINT:
		print ("CTRL+C will not work, send me a KILL signal to stop, but before that, make me write Hello")
		print ("Send me one of the following signals {}".format (", ".join (str(int(s)) for s in signals)))
	elif sig_number == signal.SIGSEGV:
		sys.stdout.write ("H")
		sys.stdout.flush ()
	elif sig_number == signal.SIGTSTP:
		sys.stdout.write ("e")
	elif sig_number == signal.SIGTTIN:
		sys.stdout.write ("l")
	elif sig_number == signal.SIGURG:
		sys.stdout.write ("o")
	elif sig_number == signal.SIGXCPU:
		sys.stdout.write ("\n")
		stop = True
	else:
		print ("Got signal {}".format (sig_number))
		

for s in range(0, signal.NSIG):
	try:
		signal.signal (s, signal_handler)
	except:
		pass

print ("My PID is {}, send me a signal".format (os.getpid ()))

while not stop:
	pass