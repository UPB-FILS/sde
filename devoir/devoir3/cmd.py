import parse

# Internal change-directory command.
def shell_cd (dir):
    # TODO - execute cd
    pass

# Internal exit/quit command.
def shell_exit ():
    # TODO - execute sys.exit()
    pass

# Execute simple command
def run_simple_command (simple_command, father_command):
    # TODO - extract command and arguments; ATTENTION! not all commands are simple_commands
    # TODO - extract redirects from father_command
    # TODO - fork parent process
    # TODO - execute child
    # TODO - wait for child
    # TODO - return exit status
    pass

# Process two commands in parallel, by creating two children.
def do_in_parallel (cmd1, cmd2, father_command):
    # TODO - execute cmd1 and cmd2 simultaneously
    pass

def do_on_pipe (cmd1, cmd2, father_command):
    # TODO - redirect the output of cmd1 to the input of cmd2
    pass

#Parse and execute a command.
def parse_command (command):
    if command.op == parse.OP_NONE:
        # TODO - run a simple command
        return run_simple_command (command.commands, command)
    elif command.op == parse.OP_SEQUENTIAL:
        # TODO - execute the commands one after the other
        pass
    elif command.op == parse.OP_PARALLEL:
        # TODO - execute the commands simultaneously
        pass
    elif command.op == parse.OP_CONDITIONAL_NZERO:
        # TODO - execute the second command only if the first one returns non zero
        pass
    elif command.op == parse.OP_CONDITIONAL_ZERO:
        # TODO - execute the second command only if the first one returns zero
        pass
    elif command.op == parse.OP_PIPE:
        # TODO - redirect the output of the first command to the input of the second
        return 0 # TODO - replace with actual exit code of command
    

try:
    while True:
        line = input('$')
        command = parse.parse(line)
        # print the resulting object, for debugging only
        parse.dump(command) # TODO - delete the line before submitting the homework
        parse_command (command)
except EOFError:
    pass