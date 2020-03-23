import os

try:
    
    # TODO 1 run ls -l using fork and execl
    pid = os.fork()
    if pid == -1:
        print ('Fork error')
    elif pid == 0:
        # TODO 1 make sure you find where the ls command is (hint: which ls)
        os.execl ('/bin/ls', '/bin/ls', '-l')
    else:
        # TODO 3
        (pid,status) = os.waitpid (pid,0)

    # TODO 2 make sure this line is printed AFTER ls is run (hint: waitpid)
    print ("ls was run")

    # TODO 3 move the print line so that it prints the exit code of ls
    print ("ls was run and exited with result {}".format(os.WEXITSTATUS (status)))

    # TODO 4 run the exitcode.py program with fork, exec and waitpid
    pid = os.fork ()
    if pid == -1:
        print ('Fork error')
    elif pid == 0:
        os.execlp ('python3', 'python3', 'exitcode.py')
    else:
        (pid,status) = os.waitpid (pid,0)
        print ("exitcode.py was run and exited with result {}".format(os.WEXITSTATUS (status)))

except Exception as e:
    print ("Error: {}".format (e))