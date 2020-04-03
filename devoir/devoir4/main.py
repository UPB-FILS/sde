from process import *
import sys

SCHEDULER_PID = 0
MAX_PID = 99

def number_processes ():
    # TODO - return the number of processes
    return 0

def next_free_pid ():
    # TODO - generate next available pid
    return 1

args = sys.argv[1:]
if len(args) >= 3:
    algorithm = args[0]
    quantum = int (args[1])
    first_process = args[2]

    # start the scheduler process
    scheduler = Process (0, '')

    # start the first process from the command line
    pid = next_free_pid()
    process = Process (pid, first_process)

    # While the number of processes is greater than 1 (there is at least one extra process)
    while number_processes() > 1:
        # select the next process to run based on one of the algorithms (read from argv)
        status = process.run ()
        if status == Process.PROCESS_PREEMPTED:
            # The process was premepted
            pass
        elif status == Process.PROCESS_SYSCALL:
            # The process asked a syscall from  PROCESS_SYSCALL_SLEEP, PROCESS_SYSCALL_FORK, PROCESS_SYSCALL_END
            if process.syscall == Process.PROCESS_SYSCALL_SLEEP:
                print ("Sleep process {}, {}".format (process.pid, process.sleep)) # do not delete this line
                pass
            elif process.syscall == Process.PROCESS_SYSCALL_FORK:
                # create new process
                print ("Fork process {}, {}", process.pid, process.extra) # do not delete this line
                pass
            elif process.syscall == Process.PROCESS_SYSCALL_END:
                process.end()
        else:
            # The process has an error, stop it
            process.end()
            pass
else:
    print ("Invalid program run")
