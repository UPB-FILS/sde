import os

def wait_for_input(msg):
	print (msg)
	input (" -- Press ENTER to continue ...")
	


wait_for_input("beginning")

try:
    #open files
    fd1 = os.open("tmp1.txt", os.O_CREAT | os.O_RDWR, 0o644)
    wait_for_input("created tmp1.txt")

    fd2 = os.open("Makefile", os.O_RDONLY)
    wait_for_input("opened Makefile")

    #redirect stderr to fd1 
    wait_for_input("redirect stderr")
    os.dup2(fd1,2)

	# write something to stderr
    b_something = bytes ("something", "utf-8")
    rc = 0
    while (rc < len(b_something)):
        rc = rc + os.write(2, b_something[rc:])


    wait_for_input("dup - redirected stderr to fd1. Written "
                       "something to STDERR_FILE. Inspect the associated file.")

    os.close(fd1)
    wait_for_input("closed fd1")

	#redirect stderr to fd2
    os.dup2(fd2, 2)
    wait_for_input("dup2 - redirected stderr to fd2")

    os.close(fd2)
    wait_for_input("closed fd2")
except Exception as e:
    print ("Error: {}".format (e))