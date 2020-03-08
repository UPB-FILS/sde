import os

try:
    
    # TODO 1 run ls -l using fork and execl
    if pid == -1:
        print ('Fork error')
    elif pid == 0:
        # TODO 1 make sure you find where the ls command is (hint: which ls)
        pass
    else:
        # TODO 3
        pass

    # TODO 2 make sure this line is printed AFTER ls is run (hint: waitpid)
    print ("ls was run")

    # TODO 3 move the printf line so that it prints the exit code of ls
    print ("ls was run and exited with result {}".format(os.WEXITSTATUS (status)))

    # TODO 4 compile the exitcode.c program, run it with fork, exec and waitpid

except Exception as e:
    print ("Error: {}".format (e))