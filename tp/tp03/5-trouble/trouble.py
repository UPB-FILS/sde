import os 

msg = "Ana are mere!\n"

# opening files
# Hint: use ls -l
try:
    fd = os.open("tmp1.txt", os.O_CREAT | os.O_WRONLY)
    # write something to stderr
    b_msg = bytes (msg, "utf-8")
    rc = 0
    while (rc < len(b_msg)):
        rc = rc + os.write(2, b_msg[rc:])

    os.close(fd)
except Exception as e:
    print ("Error: {}".format (e))