import os
import sys

BUFSIZE = 10

# len (sys.argv) - the number of arguments (command line) that the program received
# sys.argv - array of strings with the arguments
# sys.argv[0] - program name
# sys.argv[1] - first argument

argc = len (sys.argv)

if (argc < 2 or argc > 3):
	print ("Usage:\n\t " + sys.argv[0]+ " source_file [destination_file]")
	sys.exit (0)

in_file = sys.argv[1]
try:
	fd1 = os.open(in_file, os.O_CREAT | os.O_RDWR, 0o644)

	if (argc == 2):
		b_msg = os.read(fd1, BUFSIZE)
		rc = 0
		while (rc < len(b_msg)):
			rc = rc + os.write(1, b_msg[rc:])

		while (len (b_msg) != 0):
			b_msg = os.read(fd1, BUFSIZE)
			rc = 0
			while (rc < len(b_msg)):
				rc = rc + os.write(1, b_msg[rc:])		
	elif (argc == 3):
		out_file = sys.argv[2]
		fd2 = os.open(out_file, os.O_CREAT | os.O_RDWR, 0o644)
		b_msg = os.read(fd1, BUFSIZE)
		rc = 0
		while (rc < len(b_msg)):
			rc = rc + os.write(fd2, b_msg[rc:])

		while (len (b_msg) != 0):
			b_msg = os.read(fd1, BUFSIZE)
			rc = 0
			while (rc < len(b_msg)):
				rc = rc + os.write(fd2, b_msg[rc:])
		os.close (fd2)
	os.close (fd1)
except Exception as e:
		print ("Error: {}".format (e))