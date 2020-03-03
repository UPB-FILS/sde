import sys

while True:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
        d = int(sys.argv[4])
        print ( a + b * c + d)
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        break

