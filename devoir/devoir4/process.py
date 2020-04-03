class Process:
    PROCESS_OK = 0
    PROCESS_PREEMPTED = 1
    PROCESS_SYSCALL = 2
    PROCESS_ERROR_INSTRUCTION_EXCEPTION = -2
    PROCESS_ERROR_FILENAME_ACCESS = -2

    PROCESS_SYSCALL_SLEEP = 1
    PROCESS_SYSCALL_FORK = 2
    PROCESS_SYSCALL_END = 3

    def __init__ (self, pid, filename):
        self.pid = pid
        self.quantum = 0
        self.units = 0
        self.syscall = -1
        self.sleep = 0
        self.extra = ''
        
        if self.pid == 0:
            print ("Start process {}".format (pid))
        elif (self.pid != 0) and (len(filename) > 0):  
            try:
                self.file = open (filename, 'r')
                print ("Start process {}".format (pid))
            except IOError:
                print ("Could not open file: {}".format (filename))
        else:
            print ("Process start incorrect parameters")
        
    def __run (self):
        if self.units <= self.quantum:
            print ("  run units {}".format (int (self.units)))
            self.quantum = self.quantum - self.units
            self.units = 0
        else:
            print ("  run units {}".format (int (self.quantum)))
            self.units = self.units - self.quantum
            self.quantum = 0

    def __fetch_instr (self):
        if self.pid != 0:
            l = '\n'
            while l == '\n':
                l = self.file.readline ()
            if l == '':
                return 'EOF'
            else:
                return l.rstrip()
        else:
            if self.sleep == 0:
                ret_val =  "p 1"
            else:
                ret_val =  "s 1"

            self.sleep = 1 - self.sleep
            return ret_val
    
    def run (self, quantum):
        print ("Running process {}".format (self.pid))

        error = self.PROCESS_OK
        self.quantum = quantum
        # still has cycles to run
        while (self.quantum > 0) and (error == self.PROCESS_OK):
            if self.units > 0:
                self.__run ()
            if (self.units == 0) and (self.quantum > 0):
                instruction_line = self.__fetch_instr ()
                if instruction_line != '':
                    tokens = instruction_line.split ()
                    if len (tokens) >= 2:
                        print ("  instr {}, {}".format(tokens[0], tokens[1]))
                        instruction = tokens[0]
                        try:
                            units = int (tokens[1])

                            if units > 0:
                                if instruction == 'p':
                                    self.units = units
                                elif instruction == 's':
                                    self.sleep = units
                                    self.syscall = self.PROCESS_SYSCALL_SLEEP
                                    error = self.PROCESS_SYSCALL
                                else:
                                    error = self.PROCESS_ERROR_INSTRUCTION_EXCEPTION
                        except:
                            if instruction == 'f':
                                self.extra = tokens[1]
                                self.syscall = self.PROCESS_SYSCALL_FORK
                                error = self.PROCESS_SYSCALL
                            else:
                                error = self.PROCESS_ERROR_INSTRUCTION_EXCEPTION
                    else:
                        if instruction_line == "EOF":
                            self.syscall = self.PROCESS_SYSCALL_END
                            error = self.PROCESS_SYSCALL
                        else:
                            error = self.PROCESS_ERROR_INSTRUCTION_EXCEPTION
                else:
                    error = self.PROCESS_ERROR_FILENAME_ACCESS
        if (self.quantum == 0) and (error == self.PROCESS_OK):
            print ("Preempted process {}".format (self.pid))
            error = self.PROCESS_PREEMPTED
        elif error == self.PROCESS_SYSCALL:
            print ("Syscall process {}, syscall number {}".format (self.pid, self.syscall))
        return error

    def end (self):
        print ("End process {}".format (self.pid))

            




    
