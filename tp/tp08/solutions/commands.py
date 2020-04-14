import os
import threading
import queue

commands = queue.Queue()

def starter ():
	while True:
		print ("Starter waiting for command")
		cmd = commands.get ()
		print ("Executing command {}".format (cmd))
		pid = os.fork ()
		if pid == 0:
			os.execvp (cmd[0], cmd)
		else:
			os.waitpid (pid, 0)
			commands.task_done()
	print ("Started exiting, no more commands")

t = threading.Thread(target=starter, daemon=True)
t.start()

exit = False
while not exit:
	commands.join ()
	cmd = input ("$ ")
	if cmd == "exit":
		exit = True
	else:
		commands.put (cmd.split (' '))

