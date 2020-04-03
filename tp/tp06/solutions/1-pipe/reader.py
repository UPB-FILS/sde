#!/usr/bin/python3
import os

BUFFER_SIZE = 100

# TODO 2 read from stdin (fd 0) and print on the screen
buffer = os.read (0, BUFFER_SIZE)
print ("Reader read from stdin (fd 0): {}".format (str (buffer, "utf-8")))
