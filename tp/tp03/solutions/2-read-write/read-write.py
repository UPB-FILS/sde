import os

try:
    #TODO 1
    name = "my name\n"
    
    b_name = bytes(name, "utf-8")
    rc = 0
    while (rc < len(b_name)):
        rc = rc + os.write(1, b_name[rc:])

    #TODO 2
    b_name = os.read(0, 100)
    rc = 0
    while (rc < len(b_name)):
        rc = rc + os.write(1, b_name[rc:])
    
    #TODO 3
    fd = os.open("output.txt", os.O_CREAT | os.O_RDWR, 0o644)
    os.dup2(fd,1)
    print (name)
    os.close (fd)
except Exception as e:
    print ("Error: {}".format (e))

