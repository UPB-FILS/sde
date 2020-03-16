import bashlex

OP_CONDITIONAL_NZERO = 0
OP_CONDITIONAL_ZERO = 1
OP_SEQUENTIAL = 2
OP_PARALLEL = 3
OP_NONE = 4
OP_PIPE = 5

class Command:
    def __init__(self):
        self.op = OP_NONE
        self.com1 = None
        self.com2 = None
        self.commands = []
        self.input = None
        self.output = None
        self.err = None
        self.append_err = False
        self.append_out = False

class SimpleCommand:
    def __init__(self, word):
        self.word = word

class Redirect:
    IN = 0
    OUT = 1
    ERR = 2
    OUT_ERR = 3
    APPEND_OUT = 4
    APPEND_ERR = 5
    APPEND_OUT_ERR = 6

    def __init__(self, redirect_type, redirect_file):
        self.type = redirect_type
        self.file = redirect_file

def parseNode (node, redirects):
    if node.kind == 'list':
        command = Command()
        command.com1 = parseNode (node.parts[0], redirects)
        command.op = parseNode (node.parts[1], None)
        del node.parts[1]
        del node.parts[0]
        if len(node.parts) > 1:
            command.com2 = parseNode (node, redirects)
        else:
            command.com2 = parseNode (node.parts[0], redirects)
        return command
    elif node.kind == 'operator':
        if (node.op) == '&&':
            return OP_CONDITIONAL_NZERO
        elif (node.op) == '||':
            return OP_CONDITIONAL_ZERO
        elif (node.op) == ';':
            return OP_SEQUENTIAL
        elif (node.op) == '&':
           return OP_PARALLEL
    elif node.kind == 'pipeline':
        command = Command()
        command.com1 = parseNode (node.parts[0], None)
        command.op = OP_PIPE
        del node.parts[1]
        del node.parts[0]
        if len(node.parts) > 1:
            command.com2 = parseNode (node, redirects)
        else:
            command.com2 = parseNode (node.parts[0], redirects)
        return command
    elif node.kind == 'compound':
        return parseNode (node.list[1], node.redirects)
    elif node.kind == 'command':
        command = Command()
        if redirects:
            for redirect in redirects:
                redir = parseNode (redirect, None)
                if redir.type == Redirect.IN:
                    command.input = redir.file
                elif redir.type == Redirect.OUT:
                    command.output = redir.file
                elif redir.type == Redirect.ERR:
                    command.err = redir.file
                elif redir.type == Redirect.OUT_ERR:
                    command.err = redir.file
                    command.output = redir.file
                elif redir.type == Redirect.APPEND_ERR:
                    command.err = redir.file
                    command.append_err = True
                elif redir.type == Redirect.APPEND_OUT:
                    command.output = redir.file
                    command.append_out = True
                elif redir.type == Redirect.APPEND_OUT_ERR:
                    command.output = redir.file
                    command.err = redir.file
                    command.append_err = True
                    command.append_out = True
        for part in node.parts:
            if part.kind == 'word' and (not part.parts):
                command.commands.append (SimpleCommand(part.word))
            elif part.kind == 'redirect':
                redir = parseNode (part, None)
                if redir.type == Redirect.IN:
                    command.input = redir.file
                elif redir.type == Redirect.OUT:
                    command.output = redir.file
                elif redir.type == Redirect.ERR:
                    command.err = redir.file
                elif redir.type == Redirect.OUT_ERR:
                    command.err = redir.file
                    command.output = redir.file
                elif redir.type == Redirect.APPEND_ERR:
                    command.err = redir.file
                    command.append_err = True
                elif redir.type == Redirect.APPEND_OUT:
                    command.output = redir.file
                    command.append_out = True
                elif redir.type == Redirect.APPEND_OUT_ERR:
                    command.output = redir.file
                    command.err = redir.file
                    command.append_err = True
                    command.append_out = True
            elif part.kind == 'word' and len (part.parts) > 0:
                print (part.parts[0])
                command.commands.append (parseNode (part.parts[0], None))
        return command
    elif node.kind == 'redirect':
        if (node.type == '>' and node.input == 2):
            return Redirect(Redirect.ERR, node.output.word)
        elif (node.type == '>'):
            return Redirect(Redirect.OUT, node.output.word)
        elif (node.type == '&>'):
            return Redirect(Redirect.OUT_ERR, node.output.word)
        elif (node.type == '<'):
            return Redirect(Redirect.IN, node.output.word)
        elif (node.type == '>>' and node.input == 2):
            return Redirect (Redirect.APPEND_ERR, node.output.word)
        elif (node.type == '>>'):
            return Redirect(Redirect.APPEND_OUT, node.output.word)
        elif (node.type == '&>>'):
            return Redirect(Redirect.APPEND_OUT_ERR, node.output.word)
    elif node.kind == 'commandsubstitution' or node.kind == 'processsubstitution':
        return parseNode (node.command, redirects)           

def dump(obj):
    if isinstance(obj, Command):
        print (obj.__dict__)
        if obj.com1:
            print ('com1:')
            dump (obj.com1)
        if obj.com2:
            print ('com2:')
            dump (obj.com2)
        print ('commands:')
        for c in obj.commands:
            dump (c)
    elif isinstance (obj, SimpleCommand):
        print (obj.word)

def parse(cmd):
    parts = bashlex.parse (cmd)
    return parseNode(parts[0], None)