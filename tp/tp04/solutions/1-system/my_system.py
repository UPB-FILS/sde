
import sys
import os

if (len(sys.argv) != 2):
	print("Usage: python3 my_system.py cmd")
else:
	try:
		#ret = os.system(sys.argv[1])
		# TODO 1 - replace system with execvp (Hint: keep in mind that the first argument is the program name)
		os.execvp (sys.argv[1], sys.argv[1:])
	except Exception as e:
		print ("Error: {}".format (e))
