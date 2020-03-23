import os

# TODO 1 - use system to run program with two arguments a, b
os.system ('python3 program.py a b')
print ("System done")

# TODO 2 - use execl in the right way 
os.execlp('python3', 'python3', 'program.py', 'a', 'b')
print ("execl done")
# Why is this not printed?
