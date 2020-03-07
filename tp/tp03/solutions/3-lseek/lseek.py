import os

try:
    fd1 = os.open("Makefile", os.O_RDWR)

    pos = os.lseek(fd1, 100, os.SEEK_SET)

    fd2 = os.dup(fd1)

    pos = os.lseek(fd2, 100, os.SEEK_CUR)

    # print("pos = " + pos);

    os.close(fd1)

except Exception as e:
    print ("Error: {}".format (e))

