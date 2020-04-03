#!/usr/bin/python3
import os

BUFFER_SIZE = 100

p = os.pipe ()
pid = os.fork ()

if pid == 0:
	# this is the child
	# TODO 1 close write end of pipe, read buffer from parent, display data
	os.close (p[1])

	# buffer = os.read (p[0], BUFFER_SIZE)
	# print ("Got from parent: {}".format (str (buffer, "utf-8")))
        
	# TODO 1 close the read end of the pipe\
	# os.close (p[0])

	# TODO 2 redirect stdin to the pipe read end and run reader 
	# os.dup2 (p[0], 0)
	# os.execvp ("python3", ["python3", "reader.py"])
else:
	# this is the parent
	buffer = bytes(input ("data: "), "utf-8")
	
	# TODO 1 close read end of pipe, write buffer to child, wait for child to exit
	os.close (p[0])
	os.write (p[1], buffer)

	os.waitpid (pid, 0)
