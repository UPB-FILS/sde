#!/usr/bin/python3
import os

BUFFER_SIZE = 100

p = os.pipe ()
pid = os.fork ()

if pid == 0:
	# this is the child
	# TODO 1 close write end of pipe, read buffer from parent, display data
        
	# TODO 1 close the read end of the pipe

	# TODO 2 redirect stdin to the pipe read end and run reader 
	
else:
	# this is the parent
	buffer = bytes(input ("data: "), "utf-8")
	
	# TODO 1 close read end of pipe, write buffer to child, wait for child to exit
	
