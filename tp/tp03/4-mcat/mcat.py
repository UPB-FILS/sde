import os
import sys

# len (sys.argv) - the number of arguments (command line) that the program received
# sys.argv - array of strings with the arguments
# sys.argv[0] - program name
# sys.argv[1] - first argument

argc = len (sys.argv)

if (argc < 2 or argc > 3):
	print ("Usage:\n\t " + sys.argv[0]+ " source_file [destination_file]")
    return 0

#TODO 1 - open source file for reading 

if (argc == 3):
	#TODO 2 - redirect stdout to destination file


# TODO 1 - read from file and print to stdout
# use _only_ read and write functions

# TODO 1 - close file
